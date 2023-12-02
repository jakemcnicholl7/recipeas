BASE_DIRECTORY=/home/ec2-user
DEPLOYMENT_DIRECTORY=/opt/codedeploy-agent/deployment-root/$DEPLOYMENT_GROUP_ID/$DEPLOYMENT_ID/deployment-archive
WORKPLACE=$BASE_DIRECTORY/workplace
PROJECT=$WORKPLACE/$APPLICATION_NAME
WEBSITE="taitneamh.ie"
USER="ec2-user"

# Reset Home directory
export HOME=$BASE_DIRECTORY

# Load bashrc
source $BASE_DIRECTORY/.bashrc

# Workplace Setup
rm -rf $WORKPLACE
mkdir -p $WORKPLACE
ln -sf $DEPLOYMENT_DIRECTORY $PROJECT


# Fetch config
echo "[INFO] Fetching config"
CONFIG=$(aws secretsmanager get-secret-value --secret-id RecipeasConfiguration --query SecretString)

# Create .env file 
cd $PROJECT
echo $CONFIG | jq -r | jq -r 'to_entries[] | "\(.key)=\"\(.value)\""' > .env

# Export config values
echo $CONFIG | jq -r | jq -r 'to_entries[] | "export \(.key)=\"\(.value)\""' > config_export.sh
source ./config_export.sh
rm -f ./config_export.sh

# Install pipenv
if pipenv --version; then
	echo "[INFO] pipenv already installed"
else
	echo "[INFO] installing pipenv"
	sudo yum -y install python3-pip
	sudo -H -u $USER pip install pipenv
	source $BASE_DIRECTORY/.bashrc
	echo "[INFO] pipenv installed"
fi

# Install pyenv (necessary for python installation)

if pyenv -v; then
	echo "[INFO] pyenv already installed"
else
	echo "[INFO] installing pyenv"
	sudo yum -y install git gcc zlib-devel bzip2-devel readline-devel sqlite-devel openssl-devel
	git clone https://github.com/pyenv/pyenv.git $BASE_DIRECTORY/.pyenv
	echo "export PYENV_ROOT=\"\$HOME/.pyenv\"" >> $BASE_DIRECTORY/.bashrc
	echo "export PATH=\"\$PYENV_ROOT/bin:\$PATH\"" >> $BASE_DIRECTORY/.bashrc
	echo "if command -v pyenv 1>/dev/null 2>&1; then" >> $BASE_DIRECTORY/.bashrc
	echo "	eval \"\$(pyenv init -)\"" >> $BASE_DIRECTORY/.bashrc
	echo "fi" >> $BASE_DIRECTORY/.bashrc
	source $BASE_DIRECTORY/.bashrc
fi

# Install nginx
if nginx -v; then
	echo "[INFO] nginx already installed"
else
	echo "[INFO] installing nginx"
	sudo yum -y install nginx
fi

# Install HTTPS encryption tools
if sudo [ -d /opt/certbot ]; then
	echo "[INFO] certbot already installed"
else
	echo "[INFO] Installing certbot"
	sudo dnf install -y augeas-libs
	sudo python3 -m venv /opt/certbot/
	sudo /opt/certbot/bin/pip install --upgrade pip
	sudo /opt/certbot/bin/pip install certbot certbot-nginx
	sudo ln -sf /opt/certbot/bin/certbot /usr/bin/certbot
	echo "[INFO] certbot intalled"
fi

# Deactivate Existing Server 
echo "[INFO] Shutting down the server"
sudo systemctl stop nginx
sudo pkill gunicorn

# Configure nginx 
echo "[INFO] Configuring nginx"
sudo rm -f /etc/nginx/conf.d/nginx.conf
sudo ln -sf $PROJECT/nginx_basic.conf /etc/nginx/conf.d/nginx.conf

# Start python virtual environment
echo "[INFO] Syncing python runtime dependencies"
cd $PROJECT
if [ ! $(pipenv --venv) ]; then 
	echo "[INFO] Setting up pipenv virtual env for the first time"
	yes | pipenv install
fi
pipenv sync

# Run Application Internally
echo "[INFO] Running server locally"
pipenv run gunicorn -c gunicorn_config.py src.api:application --daemon

# Run Applicaiton Externally
echo "[INFO] Running server externally"
sudo systemctl start nginx
sudo systemctl enable nginx

# Check HTTPS connection
url="https://$WEBSITE" 
response=$(curl -s -o /dev/null -w "%{http_code}" "$url")

# Setup HTTPS encryption
if [ "$response" -ge 200 ] && [ "$response" -lt 300 ]; then
	echo "[INFO] SUCCESS HTTPS is already setup"
else
	echo "[INFO] Setting up HTTPS encryption"
	sudo certbot --nginx -d $WEBSITE -d www.$WEBSITE --agree-tos -n -m $EMAIL
	echo "0 0,12 * * * root /opt/cerbot/bin/python -c 'import random; import time; time.sleep(random.random() * 3600)'" | sudo tee -a /etc/crontab > /dev/null
	echo "[INFO] Reloading nginx config"
	sudo nginx -s reload

	# Ensure HTTPS is now running
	url="https://$WEBSITE"  
	response=$(curl -s -o /dev/null -w "%{http_code}" "$url")
	if [ "$response" -ge 200 ] && [ "$response" -lt 300 ]; then
		echo "[INFO] SUCCESS HTTPS connection setup"
	else
		echo "[ERROR] Failed to setup HTTPS connection"
		exit 1
	fi
fi






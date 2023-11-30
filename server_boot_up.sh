HOME=/home/ec2-user/
DEPLOYMENT_DIRECTORY=/opt/codedeploy-agent/deployment-root/$DEPLOYMENT_GROUP_ID/$DEPLOYMENT_ID/deployment-archive
WORKPLACE=$HOME/workplace
PROJECT=$WORKPLACE/$APPLICATION_NAME
WEBSITE="taitneamh.ie"

log () {
	echo $1 >> $HOME/deployment.log
}

# Load bashrc
source $HOME/.bashrc

# Workplace Setup
rm -r $WORKPLACE
mkdir -p $WORKPLACE
ln -sf $DEPLOYMENT_DIRECTORY $PROJECT

# Create .env file 
cd $PROJECT
aws secretsmanager get-secret-value --secret-id RecipeasConfiguration --query SecretString | jq -r | jq -r 'to_entries[] | "\(.key)=\"\(.value)\""' > .env

# Install pipenv
if pipenv --version; then
	echo "[INFO] pipenv already installed"
else
	echo "[INFO] installing pipenv"
	sudo yum install python3-pip
	pip install pipenv
fi

# Install pyenv (necessary for python installation)

if pyenv -v; then
	echo "[INFO] pyenv already installed"
else
	echo "[INFO] installing pyenv"
	sudo yum -y install git gcc zlib-devel bzip2-devel readline-devel sqlite-devel openssl-devel
	git clone https://github.com/pyenv/pyenv.git $HOME/.pyenv
	echo "export PYENV_ROOT='$HOME/.pyenv'" >> $HOME/.bashrc
	echo "export PATH='$PYENV_ROOT/bin:$PATH'" >> $HOME/.bashrc
	echo "if command -v pyenv 1>/dev/null 2>&1; then"
	echo "	eval '(pyenv init -)'"
	echo "fi"
	source $HOME/.bashrc
fi

# Install nginx
if nginx -v; then
	echo "[INFO] nginx already installed"
else
	echo "[INFO] installing nginx"
	sudo yum install nginx
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
sudo ln -sf $PROJECT/nginx_basic.conf /etc/nginx/conf.d/

# Start python virtual environment
echo "[INFO] Syncing python runtime dependencies"
cd $PROJECT
source $(pipenv --venv)/bin/activate
pipenv sync

# Run Application Internally
echo "[INFO] Running server locally"
pipenv run gunicorn -c gunicorn_config.py src.api:application --daemon

# End python virtual environment
deactivate

# Run Applicaiton Externally
echo "[INFO] Running server externally"
sudo systemctl start nginx
sudo systemctl enable nginx

# Setup HTTPS encryption
if sudo [ -d  /etc/letsencrypt/live/$WEBSITE ]; then 
	echo "[INFO] Https encryption already setup"
else
	echo "[INFO] Setting up HTTPS encryption"
	sudo certbot --nginx -d taitneamh.ie -d www.taitneamh.ie --agree-tos -n
	echo "0 0,12 * * * root /opt/cerbot/bin/python -c 'import random; import time; time.sleep(random.random() * 3600)'" | sudo tee -a /etc/crontab > /dev/null
	echo "[INFO] HTTPS encryption setup"
fi






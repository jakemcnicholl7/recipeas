
### Setup HTTPS on the Server
1. Install the HTTPS certificate generator certbot
    `sudo dnf install -y augeas-libs`
    `sudo python3 -m venv /opt/certbot/`
    `sudo /opt/certbot/bin/pip install --upgrade pip`
    `sudo /opt/certbot/bin/pip install certbot certbot-nginx`
    `sudo ln -s /opt/certbot/bin/certbot /usr/bin/certbot`
    // Reffernce instructions - https://certbot.eff.org/instructions?ws=nginx&os=pip
1. Enable http traffic to the EC2 instance
2. Obtain a nginx ssl certificate
    `sudo certbot --nginx -d taitneamh.ie -d www.taitneamh.ie`
3. AutoRenew
    `echo "0 0,12 * * * root /opt/certbot/bin/python -c 'import random; import time; time.sleep(random.random() * 3600)' && sudo certbot renew -q" | sudo tee -a /etc/crontab > /dev/null`


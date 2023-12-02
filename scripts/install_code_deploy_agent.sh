# Script to install code-deploy agent on RHEL EC2 instances

sudo yum update
sudo yum install ruby
sudo yum install wget

wget https://aws-codedeploy-eu-west-1.s3.eu-west-1.amazonaws.com/latest/install
chmod +x ./install
sudo ./install auto

sudo service codedeploy-agent start
sudo systemctl enable codedeploy-agent
sudo rm ./install

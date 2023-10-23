### Automating Deployments to EC2 Instances

1. ssh to the ec2 instance
   `ssh ec2`
2. Install the following packages 
   `sudo yum update`
   `sudo yum install ruby`
   `sudo yum install wget`
3. Install the code deploy agent
   `wget https://aws-codedeploy-eu-west-1.s3.eu-west-1.amazonaws.com/latest/install`
   `chmod +x ./install `
   `sudo ./install auto`
4. Start the agent
   `sudo service codedeploy-agent start`
5. Verify it is running
   `sudo service codedeploy-agent status`
6. Enable it to start on boot
   `sudo systemctl enable codedeploy-agent`


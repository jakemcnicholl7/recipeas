
HOME=/home/ec2-user/

log () {
	echo $1 >> $HOME/deployment.log
}

HOME=/home/ec2-user/
log $HOME 
DEPLOYMNET_DIRECTORY=/opt/codedeploy-agent/deployment-root/$DEPLOYMENT_GROUP_ID/$DEPLOYMENT_ID/deployment-archive
log $DEPLOYMENT_DIRECTORY
WORKPLACE=$HOME/workplace
log $WORKPLACE
PROJECT=$WORKPLACE/$APPLICATION_NAME
log $PROJECT
WEBSITE="taitneamh.ie"
log $WEBSITE


# Load bashrc
source $HOME/.bashrc

# Workplace Setup
rm -r $WORKPLACE
mkdir -p $PROJECT
ln -sf $DEPLOYMENT_DIRECTORY $PROJECT

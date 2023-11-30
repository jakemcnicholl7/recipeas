PROJECT_TITLE=recipeas
DEPLOYMENT_DIRECTORY=$pwd
WORKPLACE=$HOME/workplace
PROJECT=$WORKPLACE/$PROJECT_TITLE
WEBSITE="taitneamh.ie"

echo "HERE" >> test_deployment_log.txt

# Load bashrc
source $HOME/.bashrc

# Workplace Setup
rm -r $WORKPLACE
mkdir -p $WORKPLACE
ln -sf $DEPLOYMENT_DIRECTORY $WORKPLACE 

# ### OVERVIEW ###
# The server_boot_up.sh file is a that is run on EC2 instances to boot up the recipeas server.
# The server_boot_up.sh gets automatically run during deployments as specifed in the "appspec.yml" file
# 
# Testing the server_boot_up.sh is difficult as it relies on the use of ENVIRONMENT variabled that are set at runtime 
# during the Recipeas deployment to EC2 instances.
#
# See a list of the usable environment variables here ->
# 
# ### PURPOSE ###
# This test_server_boot_up.sh file is intended to simulate the running of the server_boot_up.sh file in the event 
# there is a failure in deployments to Recipeas servers. This bash script can then be run from the EC2 instance to debug the issue.
# 
# ### RUNNING INSTRUCTIONS ###
# Before running set the correct environment variable names ... see here -> for guidance
# Use the following command to run the file (this replicates how it is run during deployments)
# `sudo bash test_server_boot_up.sh`

export APPLICATION_NAME=recipeas
export DEPLOYMENT_ID=d-PBMSTHJU2
export DEPLOYMENT_GROUP_ID=7c7f2fda-55d8-41e1-a4c5-251024e4e03d

source ./server_boot_up.sh

cd ~

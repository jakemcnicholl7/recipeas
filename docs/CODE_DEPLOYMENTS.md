### Automating Deployments to EC2 Instances

A code deployment pipeline is already set up for recipeas.
When provisioning a new EC2 host the code deployment agent must be installed in order for code deployments to work.

Follow the below instuctions to install code deploy agent on the host.

### Instuctions
* (1) Using SCP copy the install_code_deploy_agent.sh script (located in the scripts folder) to the Recipeas Server
    * Example
```
scp ./scripts/install_code_deploy_agent.sh recipeas-server:/home/ec2-user
```
* (2) Run the installation script on the host
```
ssh recipeas-server
source ./install_code_deploy_agent.sh
```


### Migration to a new host for the recipeas sevrver

These instructions describe how to migrate the Recipeas EC2 sever to a new host.

Note this process involves taking down the entire server ... which is okay for now (as there are no customers).
If this is expanded we should transfer to using load balancing + kubernets and docker.

Note currently the architecture isn't horizontally scalable so only one host can be used for the Recipeas Server.
Prior to switching traffic to the new host the existing hosts must be terminiated.


### Instructions

* (1) Launch a new EC2 host
    * Use an Amazon Linux host with 64-bit (x86) Architecture
    * Use an existing Recipeas ssh key pair and security group
    * Add the Recipeas host identifier key value pair as a tag to the host key=SEVRER value=RECIPEAS
    * Associate the "RecipeasServerRole" IAM role with the EC2 instance
* (2) SSH to the host and install the code deploy agent.
    * Instuctions on how to do this can be found in the CODE_DEPLOYMENTS.md file
* (3) Terminate any already existing EC2 instances hosting the recipeas server
    * Recipeas server hosts are hosts that have the key=SERVER value=RECIPEAS key value tag associated with them.
    * Note traffic to the Recipeas Server will now timeout ... as the server will be fully offline
    * Note if terminating the host is not an option simply remove the RECIPEAS key value tag from the host.
* (4) Change the DNS IP address for the the Recipeas Website "taitneamh.ie" to point to the new inctances Public IP Address
    * DNS is managed at the [Hosting Ireland Webiste](https://clients.hostingireland.ie/clientarea.php?action=domaindetails&id=233349&refresh=1#tabDNS)
    * Note it will take some time for browsers to update the new with the DNS records (by default the TTL value is 40 Hours)
        * To bpyass this issue invalidate your cache or use an incognito browser
* (5) In AWS CodePipelines redeploy the latest deployment.
    * CodePiplines is configured to deploy to hosts tagged with key=SERVER value=RECIPEAS key value tags.
    * The deployment is configured to run the "server_boot_up.sh" file which handles the installation of dependencies and starting of the server



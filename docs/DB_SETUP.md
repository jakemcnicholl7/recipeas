### Intallation

#### EC2

Intall mongoDB - https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-red-hat/#std-label-install-mdb-community-redhat-centos

To get mongosh to work - https://www.mongodb.com/community/forums/t/openssl-error-when-starting-mongosh/243323/3 

```
sudo yum remove mongodb-mongosh
sudo yum install mongodb-mongosh-shared-openssl3
sudo yum install mongodb-mongosh
```

#### Locally 

Follow this link until the end

And then run
```
sudo apt-get install mongodb
```


To start the service run 
```
sudo mongod --logpath ~/mongo_logs --fork
```


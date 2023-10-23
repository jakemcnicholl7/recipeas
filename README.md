# Meal Planning API's
## Local
### Setup
1. Ensure [pipenv](https://pipenv.pypa.io/en/latest/) is installed on your machine

1. Setup your pthon virtual envirionment:
    `pipenv sync`
1. Run the virtual environment:
    `pipenv shell`

### Runnning

1. Run the API server:
   `python -m src.api`
1. Navigate to http://127.0.0.1:5000 and make a request. 

## EC2 Instance
### Setup
1. Launch a new EC2 instance with ssh access
1. Setup the .ssh config file as follows filling in the appropriate fields
   ```
   # AWS Host Settings
   Host ec2
      HostName ec2-3-253-69-214.eu-west-1.compute.amazonaws.com
      User ec2-user
      IdentityFile ~/.ssh/recipeas-ssh-key-v2.pem
   ```
1. Ensure the ssh key cannot be edited. 
   `chmod 400 ~/.ssh/recipeas-ssh-key-v2.pem`
1. ssh to the host
   `ssh ec2`
1. Create a writeable file on the EC2 instance
   `cd /home/ec2-user`
   `sudo mkdir workplace`
   `chmod 777 workplace`
1. Copy the latest code to the instance
   `scp -r ./recipes/ ec2:/home/ec2-user/workplace/`
1. Install pip on the instance:
   `yum install python3-pip`
1. Install pipenv on the instance:
   `pip install pipenv`
1. Install pyenv on the instance:
   Instructions [here](https://gist.github.com/trongnghia203/9cc8157acb1a9faad2de95c3175aa875)
1. Clone the repository onto the host.
   `cd /home/ec2-user/workplace/`
   `git clone https://github.com/jakemcnicholl7/recipeas.git`
1. Add the appropriate ".env" file.
1. Install python and project dependencies
   `cd /home/ec2-user/workplace/recipeas/`
   `pipenv install`
1. Install nginx and enable it on boot up. Ngins docs [here](https://nginx.org/en/docs/beginners_guide.html#proxy)
   `sudo yum install nginx`
   `sudo systemctl start nginx`
   `sudo systemctl enable nginx`
1. Symlink the nginx.conf file to the niginx activation directory 
   `cd recipeas`
   `sudo ln -s $(pwd)/nginx.conf /etc/nginx/conf.d/`
   `sudo systemctl restart nginx`

### Running 
1. `gunicorn -c gunicorn_config.py src.api:application`

## Testing

#### All Tests
1. Run
   `pytest`
   or
   `pytest -s` to include printouts
   or
   `pytest tst/chef/test_integ_sous_chef.py::test_get_popular_random_meals` to run a specific test

#### Unit Tests

1. Run
   `pytest -k 'test and not test_integ'`

#### Integration Tests

1. Run
    `pytest -k 'test_integ'`
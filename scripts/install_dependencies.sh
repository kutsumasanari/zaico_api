sudo apt update
sudo apt-get update
sudo apt upgrade
sudo apt-get install python3-dev
sudo apt-get install python3-pip -y
sudo python3 get-pip.py
pip3 install virtualenv
pip3 install --upgrade setuptools
cd /home/ec2-user/zaico_api2
virtualenv environment
source environment/bin/activate
sudo apt-get -y install uvicorn
pip3 install starlette
pip3 install "fastapi[all]"
pip3 install sqlalchemy

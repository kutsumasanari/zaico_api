sudo apt update
sudo apt upgrade
sudo apt install python3-pip
sudo python3 get-pip.py
pip install virtualenv
cd /home/ec2-user/zaico_api
virtualenv environment
source environment/bin/activate
sudo apt install uvicorn
pip install fastapi
pip install sqlalchemy

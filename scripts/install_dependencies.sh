sudo apt update
sudo apt upgrade
sudo apt-get install python3-pip -y
sudo python3 get-pip.py
pip3 install virtualenv
cd /home/ec2-user/zaico_api
virtualenv environment
source environment/bin/activate
sudo apt install uvicorn
pip3 install fastapi
pip3 install sqlalchemy

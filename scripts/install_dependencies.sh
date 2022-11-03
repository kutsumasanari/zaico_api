python -m pip install --upgrade pip
pip install virtualenv
cd /home/ec2-user/zaico_api
virtualenv environment
source environment/bin/activate
sudo apt install uvicorn
pip install fastapi
pip install sqlalchemy

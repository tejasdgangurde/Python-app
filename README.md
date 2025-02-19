# Python-app
python3 --version
sudo yum install python3-pip -y
sudo pip3 install flask
python3 -m flask --version
mkdir myflaskapp && cd myflaskapp/
python3 -m venv venv
source venv/bin/activate
sudo yum install git -y
git config --global user.name "tejasdgangurde"
git config --global user.email "EmailID"
git init
git pull https://github.com/tejasdgangurde/Python-app.git
pip install -r requirements.txt
python3 app.py
Allow Traffic on Port 5000 add it into security group
http://<EC2-PUBLIC-IP>:5000

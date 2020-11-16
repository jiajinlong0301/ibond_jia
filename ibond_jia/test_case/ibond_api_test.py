from config.conf import *
from common.get_excel import *
import requests
import json

def user_login():
    for i in range(1,2):
        account,password = get_excel_inputs(i)
        api = get_excel_api(i)
        url = server_ip() + api
        data={
             'account': account,
             'password': password
            }
        r=requests.post(url=url,data=data)
        print(r.headers)
        print(r.cookies)

user_login()
# def update_params():
#        url = server_ip() + "/api/operator/update_params"
#        data={
#               "operator_instance_id": 256,
#               "params": {
#               "device": "cpu:0",
#               "learning_rate": "0.001",
#               "model_interval": "1",
#               "total_epoches": "7"}
#        }
#        url1 = requests.post(url=url,data=data,cookie=user_login())
#        print(user_login())
#        print(url1.text)
#        print(url1.status_code)
#
# update_params()

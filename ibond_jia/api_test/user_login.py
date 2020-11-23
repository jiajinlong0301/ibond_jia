from config.ip_config import *
from common.get_excel import *
import requests
import json

def user_login():
    for i in range(1, 6):
        account, password = get_excel_inputs(i)
        api = get_excel_api(i)
        url = server_ip() + api
        data={
             'account': account,
             'password': password
            }
        r=requests.post(url=url, data=data)
        # print(data)
        response=json.loads(r.text)
        # print(type(response))
        s = eval(get_excel_expection(i))
        # print(s)
        try:
            assert response == s
            print(i)
        except AssertionError:
            pass
            print(i, '断言失败')

user_login()
from config.ip_config import org_A_ip
from common.get_excel import *
from common.get_LinuxServer import *
import requests
import json

def user_login():
    for i in range(1, 6):
        account, password = get_excel_inputs(i)
        api = get_excel_api(i)
        url = org_A_ip() + api
        data={
             'account': account,
             'password': password
            }
        r=requests.post(url=url, data=data)
        response=json.loads(r.text)
        s = eval(get_excel_expection(i))
        try:
            assert response == s
            print(i,'断言成功')
        except AssertionError:
            conect = Monitor('10.58.14.33', 'tdops', 'ai123456td')
            logs = conect.link_server('pwd')
            print(i, '断言失败', logs)

user_login()
from config.headers import headers
from config.ip_config import *
import requests
import random


def project_add():
    """
    创建联邦项目
    """
    url = org_A_ip() + "/api/project/add"
    data = {
        "name": "auto_test_05",
        "data_id": 3,
        "dag_template_code": "credit_learning_dag",
        "partners": [{
            "code": "OrgA",
            "role": ""
        }, {
            "code": "OrgB",
            "role": ""
        }],
        "partnersCode": ["OrgA", "OrgB"],
        "description": "",
        "scenario_code": "credit"
    }
    res = requests.post(url=url, json=data, headers=headers())
    print(res.json())
    assert res.json()['success'] == True


project_add()

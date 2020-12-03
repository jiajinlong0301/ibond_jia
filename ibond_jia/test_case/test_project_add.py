from config.headers_A import headers
from config.ip_config import *
import requests
import random


def test_project_add():
    """
    创建联邦项目
    """
    urla = org_A_ip() + "/api/project/add"
    data = {
        "name": "auto_test_06",
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
    res = requests.post(url=urla, json=data, headers=headers())
    print(res.json())
    assert res.json()['success'] == True


def test_project_invite_handle_accept():
    """
    接受联邦请求
    :return:
    """
    urlb = org_B_ip() + "/api/project/invite_handle/accept"
    data = {
        "project_id": 47,
        "project_name": "auto_test_06",
        "operator_org_name": "机构A",
        "data_id": 5
    }
    res = requests.post(url=urlb, data=data, headers=headers())
    print(res.json())
    assert res.json()['success'] == True
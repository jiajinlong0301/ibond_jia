from config.headers import headers
from config.ip_config import org_B_ip
import requests




def project_add():
    """
    创建联邦项目
    """
    url = org_B_ip() + "/api/project/invite_handle/accept"
    data = {
        "project_id": 44,
        "project_name": "auto_test_05",
        "operator_org_name": "机构A",
        "data_id": 5
    }
    res = requests.post(url=url, json=data, headers=headers())
    print(res.json())
    # assert res.json()['success'] == True


project_add()

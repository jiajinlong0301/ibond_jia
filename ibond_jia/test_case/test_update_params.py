from requests.models import Response
from config.ip_config import *
from config.headers import headers
import requests


def test_update_params():
    """
    更新算子参数
    :param header: 传入请求头
    :return:
    """
    url = org_A_ip() + "/api/operator/update_params"
    data = {
        "operator_instance_id": 1027,
        "params": {
            "device": "cpu:0",
            "learning_rate": "0.001",
            "model_interval": "3",
            "total_epoches": "7"}
    }
    res: Response = requests.post(url=url, json=data, headers=headers())
    print(res.json())
    assert res.json()['success'] == True


test_update_params()

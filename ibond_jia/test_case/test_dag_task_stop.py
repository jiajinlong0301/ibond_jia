from requests.models import Response
from config.ip_config import *
from config.headers_A import headers
import requests


def test_update_params():
    """
    更新算子参数
    :param header: 传入请求头
    :return:
    """
    url = 'http://' + org_A_ip() + ':8080' "/api/dag_task/stop"
    data = {
            "dag_task_id": 2447
    }
    res: Response = requests.post(url=url, json=data, headers=headers())
    print(res.json())
    assert res.json()['success'] == True


test_update_params()

from config.headers import headers,server_ip
import requests

def update_params():
    """
    更新算子参数
    :param header: 传入请求头
    :return:
    """
    url = server_ip() + "/api/operator/update_params"
    data = {
        "operator_instance_id": 1027,
        "params": {
            "device": "cpu:0",
            "learning_rate": "0.001",
            "model_interval": "3",
            "total_epoches": "7"}
    }
    headers()['Referer'] = 'http://10.58.14.33:8080/login'
    res = requests.post(url=url, json=data, headers=headers())
    assert res.json()['success'] == True

update_params()

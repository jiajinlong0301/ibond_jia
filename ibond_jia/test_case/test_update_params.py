from config.get_login_cookies import *
import requests

def update_params(header):
    url = server_ip() + "/api/operator/update_params"
    data = {
        "operator_instance_id": 1027,
        "params": {
            "device": "cpu:0",
            "learning_rate": "0.001",
            "model_interval": "1",
            "total_epoches": "7"}
    }
    res = requests.post(url=url, json=data, headers=header)
    print(res.text)
cookies = user_login_cookies()
header['Cookie'] = cookies
header['Referer'] = 'http://10.58.14.33:8080/model/drill'
header['X-Cf-Random'] = 'Xy8OVL/Lxm3ZJgvXEHYQ7NkMbYsDS3w6PKiu3lGVAQGRRPSRh/cL6RS17IfMtZc2nPHjjdfGImX5bY0ME7/PyeLL61StTMNIiLAVzfXualdU5n9EOt7JLMTLxapeqJU3Yp/S2DK8VsSEC1vO+G4uVSXJhGizmk6D3P7fwkYcf5U='
update_params(header)
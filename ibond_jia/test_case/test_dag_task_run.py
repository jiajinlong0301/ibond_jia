import requests
from config.conf import *
from config.headers import headers

def dag_task_run():
       url = server_ip() + "/api/dag_task/run"
       data={
              'dag_id':'802'
       }
       url1 = requests.post(url=url,json=data,headers=headers())
       print(url1.json())
       print(url1.status_code)

dag_task_run()
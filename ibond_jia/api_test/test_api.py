import requests
from common.read_excel import *

df=pd_read_excel()
for i in range(5):
    url = df['接口'].iloc[i]
    a = df['account'].iloc[i]
    p = df['password'].iloc[i]
    data = {
        'account': a,
        'password': p
    }
    r = requests.post(url, data)
    print(i, r.text)
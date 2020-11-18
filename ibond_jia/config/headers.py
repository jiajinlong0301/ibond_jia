from config.conf import *
import requests

def user_login_cookies():
    """
    获取登录用户cookie
    :return: 返回用户cookie和csrfToken
    """
    url = server_ip() + "/bridgeApi/user/login" #登录接口
    data={
         'account': 'admin',
         'password': 'ZAFWPv9tgy4/HEsujHm6JFzvL+7GW+QMVNN5S+dCpDHTF75SQ7rBlPKcqIiXbZiPHeHuJlYcNdpbKB+2llI7tK5lS4LJbfA0sEJfEw4JGuORPItoAwSaKyg23UTZ9DapuHSwEmvx6S99gCJhcFJhjre4b7KJwGxQPeg184MPcsI='
        } #登录参数
    r=requests.post(url=url,data=data) #请求登录
    res=r.json()
    csrfToken=res['data']['csrfToken']
    cookies=r.headers['Set-Cookie']
    return (cookies,csrfToken)

cookie,csrtoken=user_login_cookies()

def headers():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content - Type': 'application / json;charset = UTF - 8',
        'Cookie': cookie,
        #'Host': '10.58.14.33:8080',
        #'Origin': 'http://10.58.14.33:8080',
        'Pragma': 'no-cache',
        'Referer': 'http://10.58.14.33:8080/model/drill',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'X-Cf-Random': csrtoken,
        'X-Requested-Width': 'XMLHttpRequest'
    }
    return headers
from config.conf import *
import requests
from config.headers import headers

header = headers() #定义全局变量header
def user_login_cookies():
    """
    获取登录用户cookie
    :return: 返回用户cookie
    """
        url = server_ip() + "/bridgeApi/user/login" #登录接口
        data={
             'account': 'admin',
             'password': 'ZAFWPv9tgy4/HEsujHm6JFzvL+7GW+QMVNN5S+dCpDHTF75SQ7rBlPKcqIiXbZiPHeHuJlYcNdpbKB+2llI7tK5lS4LJbfA0sEJfEw4JGuORPItoAwSaKyg23UTZ9DapuHSwEmvx6S99gCJhcFJhjre4b7KJwGxQPeg184MPcsI='
            } #登录参数
        r=requests.post(url=url,data=data,headers=header) #请求登录
        return r.headers['Set-Cookie']
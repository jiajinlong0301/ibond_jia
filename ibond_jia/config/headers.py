def headers():
    """
    定义请求头
    :return: 返回请求头
    """
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'Host': '10.58.14.33:8080',
        'Origin': 'http://10.58.14.33:8080',
        'Referer': 'http://10.58.14.33:8080/login',
        'X-Cf-Random': 'null',
        'X-Requested-Width': 'XMLHttpRequest'
    }
    return headers
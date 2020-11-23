def org_A_sql():
    """
    连接mysql数据库
    :return:连接信息
    """
    host = '10.58.14.33'
    user = 'bond'
    password = 'bond_123456'
    database = 'bond'
    port = 3306
    charset = 'utf8'
    return host, user, password, database, port, charset


def org_B_sql():
    """
    连接mysql数据库
    :return:连接信息
    """
    host = '10.58.14.32'
    user = 'bond'
    password = 'bond_123456'
    database = 'bond'
    port = 3306
    charset = 'utf8'
    return host, user, password, database, port, charset

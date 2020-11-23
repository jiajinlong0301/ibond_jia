from config.ip_config import org_B_sql
import pymysql


def get_sql(sql):
    """
    执行sql语句
    :param sql:
    :return:查询结果
    """
    host, user, password, database, port, charset = sql_conf()  # 从模块config.conf.sql_conf方法导入
    db = pymysql.connect(host=host, user=user, password=password, database=database, port=port, charset=charset)
    cursor = db.cursor()  # 建立游标
    cursor.execute(sql)  # 执行sql
    data = cursor.fetchall()  # 保存结果
    cursor.close()
    db.close()
    return data

get_sql('select * from tm_dag order by id desc limit 5')

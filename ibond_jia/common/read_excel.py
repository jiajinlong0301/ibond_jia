import pandas as pd

def pd_read_excel():
    """
    未使用
    :return:
    """
    df = pd.read_excel("../test_data/ip_config.xlsx")  # 打开data.xlsx文件
    return df.loc[:, ['接口', 'account', 'password']]

# print(pd_read_excel())
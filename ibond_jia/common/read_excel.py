import pandas as pd

def pd_read_excel():
    """
    未使用
    :return:返回'account','password'列的所有值
    """
    df = pd.read_excel("../test_data/data.xlsx") #打开data.xlsx文件
    return df.loc[:,['account','password']]
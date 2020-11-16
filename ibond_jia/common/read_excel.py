import pandas as pd

def pd_read_excel():
    df = pd.read_excel("../test_data/data.xlsx")
    return df.loc[:,['account','password']]
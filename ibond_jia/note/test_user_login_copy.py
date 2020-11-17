from config.conf import *
from common.get_excel import *
import requests
import xlrd
import pytest
import json

def sheet_to_list(excel_file_path, sheet_name):
    lst = []
    with xlrd.open_workbook(excel_file_path) as f:
        table = f.sheet_by_name(sheet_name)
        # nrows是sheet的行数
        for row in range(0, table.nrows):
            lst.append([])
            # ncols是sheet的列数
            for col in range(0, table.ncols):
                # ctype为1是字符串，ctype为2是数值。
                cell_type = table.cell(row, col).ctype
                cell_value = table.cell_value(row, col)
                # 去掉字符串首尾空格。excel会自动去掉整数和浮点数前后的空格。
                if cell_type == 1:
                    lst[row].append(cell_value.strip())
                # xlrd读取cell时1变成1.0。如果是数值，并且原本是整数，则返回整数。
                elif cell_type == 2 and cell_value == round(cell_value):
                    lst[row].append(int(cell_value))
                # 浮点数则不用额外处理
                else:
                    lst[row].append(cell_value)
    return lst

# 从excel sheet中获取@pytest.mark.parametrize()所需要的参数名和数据
def get_data_from_sheet(excel_file_path, sheet_name):
    lst = sheet_to_list(excel_file_path, sheet_name)
    # 参数名格式化，格式为"a,b,c"
    param_name = ','.join(lst[0])
    # 去掉参数名行，剩下的就是数据
    data = lst[1:]
    return param_name, data

get_data_from_sheet('../test_data/data.xlsx', 'user_login')

# # 使用举例：
# @pytest.mark.parametrize(*get_data_from_sheet("test_data.xlsx", "add_test"))
# def test_add(a, b, c):
#     assert a + b == c

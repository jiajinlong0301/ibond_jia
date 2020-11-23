import xlrd
from xlrd import Book


def get_excel_api(row):
    """
    获取data.xlsx文件中接口列的值
    :param row:所有行
    :return:返回第一列的所有值
    """
    excel: Book = xlrd.open_workbook('../test_data/data.xlsx')  # 打开data.xlsx文件
    table = excel.sheets()[0]  # 获取第一个sheet
    return table.cell_value(row, 0)


def get_excel_inputs(row):
    excel = xlrd.open_workbook('../test_data/data.xlsx')
    table = excel.sheets()[0]
    return table.cell_value(row, 2), table.cell_value(row, 3)


def get_excel_expection(row):
    excel = xlrd.open_workbook('../test_data/data.xlsx')
    table = excel.sheets()[0]
    return table.cell_value(row, 4)
    # print(table.nrows) #总行数
    # print(table.ncols) #总列数
    # print(table.row_values(0)) #第一行数据
    # print(table.col_values(0)) #第一列数据
    # print(table.cell_value(0,1)) #第一行，第二列信息，前面是行，后面是列
    # for i in range(1,table.nrows):
    #     print(table.cell_value(i,1),table.cell_value(i,2))

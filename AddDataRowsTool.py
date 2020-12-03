#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#-----------------------------------------
# Author:  ye.liy
# Date: 2020/11/10
#-----------------------------------------
"""

import csv
import random
import QuantityStatisticsTool as q

"""
    增加数据的行数
filename:文件名
idnum:id列,从1开始
labenum：标签列，从1开始
nums：总行数
newFilename:保存的文件名
"""


def AddData(filename, newFilename,idnum, nums, labelnum=None):
    csvres = []
    with open(filename, newline="") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            csvres.append(row)
    # 获取文件行数据
    num = len(csvres)
    # 统计列数，取的是头的长度
    newrow = csvres[0]
    length = len(newrow)
    # 生成id值对应的下标
    idnum = int(idnum) - 1
    # 判断传入的标签列是否为空，如果不为空，则获取对应的标签角标
    if labelnum != None:
        reslabelnum = int(labelnum) - 1
    # 打开新文件，写入数据
    with open(newFilename, "w") as f1:
        writer = csv.writer(f1)
        # 截取对应的行数生成值
        for i in range(0, nums):
            # 如果i小于文件行数据，则将原来的文件写入
            if i < num:
                newrow = csvres[i]
                writer.writerow(newrow)
            # 如果i >= 文件的总行数，则手动造数据
            else:
                row1 = []
                for a in range(0, length):
                    # 造id列值
                    if a == idnum:
                        int1 = random.randint(0, 100000000000)
                        row1.append(int1)
                    # 生成标签值
                    elif labelnum != None and a == reslabelnum:
                        int2 = random.randint(0, 1)
                        row1.append(int2)
                    # 造其他字段数据
                    else:
                        floata1 = random.uniform(-1, 1)
                        floata1 = "%.6f" % floata1
                        row1.append(floata1)
                writer.writerow(row1)
    statis = q.QuantityStatistics(newFilename, labelnum)
    return "修改文件成功，新文件:【" + newFilename + "】的信息如下：\n" + statis


if __name__ == "__main__":
    a = AddData("a.csv","a1.csv", 1, 500, 2)
    print(a)
    b = AddData("a.csv","a2.csv", 1, 500, 2)
    print(b)

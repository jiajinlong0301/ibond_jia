#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
@author:liye
@file:QuantityStatisticsTool.py
# Date: 2020/11/10
"""
import pandas as pd
from time import *
def QuantityStatistics(filename, labelNum=None):
    # beginTime = time()
    # df = pd.read_csv(filename, encoding="utf-8")
    # resnum = df.shape
    # res = "样本名称：" + filename + "\n样本行数为：%d\n" % resnum[0] + "样本列数为：%d\n" % resnum[1]
    # if labelNum != None:
    #     # 获取文件头
    #     head = df.columns
    #     # 获取标签名字
    #     labelNum = int(labelNum) - 1
    #     labelName = head[labelNum]
    #     # 按样本标签统计数量
    #     nums = df.groupby([labelName]).count()
    #     # 通过第一列的头，获取正负样本数据
    #     num = nums[head[0]]
    #     Fnum = 0
    #     Tnum = 0
    #     # 负样本标签数据
    #     if 0 in num.index:
    #         Fnum = num[0]
    #     if 1 in num.index:
    #         # 正样本标签数据
    #         Tnum = num[1]
    #     res = res + "负样本数量是：%d\n" % Fnum + "正样本数量是：%d\n" % Tnum
    # endTime = time()
    # runTime = endTime - beginTime
    # print(runTime)
    # return res


    beginTime = time()
    df = pd.read_csv(filename, sep=',', engine='python', iterator=True)
    # 获取文件头
    headData = df.get_chunk(0)
    head = headData.columns
    cols = len(head)
    # 获取标签名字
    labelNum = int(labelNum) - 1
    labeName = head[labelNum]
    loop = True
    chunkSize = 100000
    i = 0
    rows = 0
    Fnum = 0
    Tnum = 0
    while loop:
        try:
            i = i + 1
            chunk = df.get_chunk(chunkSize)
            rows = rows + chunk.shape[0]
            if labelNum != None:
                # 获取负样本数据量
                totalData = len(chunk[labeName].values)
                TnumData = sum(chunk[labeName].values)
                FnumData = totalData - TnumData
                Fnum = FnumData + Fnum
                Tnum = TnumData + Tnum
            chunk = None
        except StopIteration:
            loop = False
            print("Iteration is stopped.")
    res = "样本名称：" + filename + "\n样本行数为：%d\n" % rows + "样本列数为：%d\n" % cols
    if labelNum != None:
        res = res + "负样本数量是：%d\n" % Fnum + "正样本数量是：%d\n" % Tnum

    endTime = time()
    runTime = endTime - beginTime
    print(runTime)

    return res
if __name__ == "__main__":
    a = QuantityStatistics("/Users/liye/Documents/code/automan/ibond-automantest/tool/lendingclub_aa_train_minmax-44w.csv", 2)
    print(a)


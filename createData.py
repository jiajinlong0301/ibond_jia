#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
@author:liye
@file:createData.py
@time:2020/11/30
'''

import random
import gc
import hashlib
import csv
import math
#import QuantityStatisticsTool as q


def CreateData(filename,nums,head,idnum,labelnum = None):
    '''

    :param filename: 生成的文件名
    :param nums: 生成的行数
    :param head: 头名，列表形式[id，label，x0]
    :param idnum: id列，从0开始
    :param labelnum: label列，从0开始；label=None则表示无标签列
    :return:
    '''

    # 打开新文件，写入数据
    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerow(head)
        lenHead = len(head)
        print(lenHead)
        str_start = ['133', '149', '153', '173', '177', '180', '181', '189', '199', '130', '131', '132', '145', '155',
                     '156', '166', '171', '175', '176', '185', '186', '166', '134', '135', '136', '137', '138', '139',
                     '147', '150', '151', '152', '157', '158', '159', '172', '178', '182', '183', '184', '187', '188',
                     '198']
        length = len(str_start)
        num = math.ceil(nums / length)
        for i in str_start:
            end = 1000000
            for n in range(0,num):
                row = []
                for a in range(0,lenHead):
                    if a == idnum:
                        end = end + 1
                        str_end = end
                        str_phone = i + str(str_end)
                        str_phone = str_phone.encode("utf8")
                        md5 = hashlib.md5()
                        md5.update(str_phone)
                        phone = md5.hexdigest()
                        row.append(phone)
                    elif a != None and a == labelnum:
                        int2 = random.randint(0, 1)
                        row.append(int2)
                    else:
                        floata1 = random.uniform(-1, 1)
                        floata1 = "%.6f" % floata1
                        row.append(floata1)
                writer.writerow(row)
                del row
                gc.collect()
            del str_end
            del str_phone
            del md5
            del phone
            gc.collect()

    # a = q.QuantityStatistics(filename)
    # print(a)

    return "修改文件成功，新文件:【" + filename + "】的信息如下：\n"

if __name__ == "__main__":
    a = CreateData('newphone.csv',100,['ID','x0','y'],0,2)


#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
@author:liye
@file:3.py
@time:2020/11/30
'''

import random
import gc
import hashlib
import csv
import math
def AddData(filename,nums,head):
    '''

    :param filename: 文件名
    :param nums: 需要生成的行数
    :param head:文件头
    :return:
    '''
    # 打开新文件，写入数据
    with open(filename, "w") as f:
        writer = csv.writer(f)
        headTitle = [head]
        writer.writerow(headTitle)
        str_start = ['133', '149', '153', '173', '177', '180', '181', '189', '199', '130', '131', '132', '145', '155',
                     '156', '166', '171', '175', '176', '185', '186', '166', '134', '135', '136', '137', '138', '139',
                     '147', '150', '151', '152', '157', '158', '159', '172', '178', '182', '183', '184', '187', '188',
                     '198']
        length = len(str_start)
        num = math.ceil(nums / length)
        for i in range(1, nums):
            end = 1000000
            for i in str_start:
                for n in range(0,num):
                    row = []
                    end = end + 1
                    str_end = end
                    str_phone = i + str(str_end)
                    str_phone = str_phone.encode("utf8")
                    md5 = hashlib.md5()
                    md5.update(str_phone)
                    phone = md5.hexdigest()
                    row.append(phone)
                    writer.writerow(row)
                del str_end
                del str_phone
                del md5
                del phone
                gc.collect()

    return "修改文件成功，新文件:【" + filename + "】的信息如下：\n"

if __name__ == "__main__":
    a = AddData('newphone.csv',5000000,'ID')

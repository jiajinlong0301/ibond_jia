import random

'''
手机号码: 13[0-9], 14[5,6,7,8,9], 15[0-3, 5-9], 16[2,5,6,7], 17[0-8], 18[0-9], 19[0-3, 5-9]

移动号段: 13[4-9],147,148,15[0-2,7-9],165,170[3,5,6],172,178,18[2-4,7-8],19[5,7,8];
联通号段: 130,131,132,145,146,155,156,166,167,170[4,7,8,9],171,175,176,185,186,196;
电信号段: 133,149,153,162,170[0,1,2],173,174[0-5],177,180,181,189,19[0,1,3,9];
广电号段: 192
'''

def create_phonenub():
    #choice the second num
    second = [3, 4, 5, 6, 7, 8, 9][random.randint(0, 6)]

    #choice the third num
    third = {
        3: random.randint(0, 9),
        4: random.randint(5, 9),
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        6: [2, 5, 6, 7][random.randint(0,3)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
        9: [i for i in range(10) if i != 4][random.randint(0, 8)],
    }[second]

    #choice the last 8 num
    suffix = random.randint(9999999, 100000000)

    return "1{}{}{}".format(second, third, suffix)


if __name__ == '__main__':
    phonenum = create_phonenub()
    print(phonenum)
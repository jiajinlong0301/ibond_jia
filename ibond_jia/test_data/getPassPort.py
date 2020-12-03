import random

'''
因私普通护照：14/15+7位数，G+8位数；
因公普通护照：P.+7位数；
公务护照：S.+7位数或者 S+8位数；
外交护照：以D开头，D=diplomatic.
'''

def create_passport():
    #choice the type
    type = random.choice(['14', '15', 'G', 'P', 'S', 'D'])

    #choice the num
    suffix = {
        '14': random.randint(999999, 10000000),
        '15': random.randint(999999, 10000000),
        'G': random.randint(9999999, 100000000),
        'P': random.randint(999999, 10000000),
        'S': random.randint(999999, 100000000),
        'D': random.randint(999999, 100000000),
    }[type]

    return "{}{}".format(type, suffix)


if __name__ == '__main__':
    passport = create_passport()
    print(passport)

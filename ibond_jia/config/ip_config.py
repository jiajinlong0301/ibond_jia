def org_A_ip():
    """
    各环境访问地址
    :return: 环境地址
    """
    algo_ip = '10.58.14.33'  # 算法环境
    test_ip = '10.57.17.251' # 测试环境
    return test_ip


def org_B_ip():
    """
    各环境访问地址
    :return: 环境地址
    """
    algo_ip = '10.58.14.32'  # 算法环境
    test_ip = '10.57.239.33' # 测试环境
    return test_ip


def main():
    print(org_A_ip(),  org_B_ip())


if __name__ == '__main__':
    main()
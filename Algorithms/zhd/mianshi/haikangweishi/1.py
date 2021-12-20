"""

 海康威视面试手撕代码，查找一个字符串中出现次数最多的元素的个数
 这里用字典的方法，将所有的的元素当作key，对应出现的次数为value，最后用sorted对字典的value排序
"""


def count_max(list):
    dict_n = {}
    for ele in list:
        if ele not in dict_n.keys():
            dict_n[ele] = 0
        dict_n[ele] += 1
    ans = sorted(dict_n.items(), key=lambda d: d[1], reverse=False)
    return ans[-1]


if __name__ == '__main__':
    # n = int(input())
    # list_n = []
    # for i in range(n):
    #     # list_n.append(list(map(float, input().strip().split())))  # 二维列表
    #     list_n.append(int(input()))  # 一维列表
    # list_n = 'abcda'
    list_n = [1,2,3,4,5,1]
    print(count_max(list_n))

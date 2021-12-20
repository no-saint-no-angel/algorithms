"""
    本文件实现堆排序
"""


def sift(li, low, high):
    """

    :param li: 列表
    :param low:  堆的根节点位置
    :param high:  堆的最后一个元素的位置
    :return:
    """
    i = low  # i最开始指向根节点
    j = 2 * i + 1  # j开始时左孩子
    tmp = li[low]
    while j <= high:  # 只要j位置有数，循环继续
        if j + 1 <= high and li[j+1] > li[j]:  # 如果右孩子有并且比较大
            j = j + 1  # j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j   # 往下再看一层
            j = 2*i+1
        else:  # temp更大，把tmp放在i的位置，
            li[i] = tmp  # 把tmp放到某一级领导的位置
            break
    else:
        li[i] = tmp  # 把tmp放到叶子节点


def heap_sort(li):
    n = len(li)
    # 首先先建堆，思想（农村包围城市）。找到最后一个非叶子节点的位置，根据最后一个叶子节点位置，根据孩子找父亲的公式
    for i in range((n-2)//2, -1, -1):
        # i代表了建堆的时候调整的根的位置
        sift(li, i, n-1)
    # 建堆完成
    for i in range(n-1, -1, -1):
        # i指向当前堆最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)  # i-1是新的high
    print('li', li)


li = [i for i in range(10)]
import random
random.shuffle(li)
print(li)

heap_sort(li)

#
# # 使用python内置的模块进行堆排序
# import heapq
# li = [i for i in range(10)]
# import random
# random.shuffle(li)
# print(li)
# heapq.heapify(li)  # 建堆， 构建的是小根堆
# for i in range(len(li)):
#     print(heapq.heappop(li), end=",")  # 每次弹出堆最小的元素


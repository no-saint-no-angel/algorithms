"""
    插入排序
"""
import random
from cal_time import cal_time


@ cal_time
def insert_search(li):
    for i in range(1, len(li)):  # 表示摸到的牌的下标
        temp = li[i]
        j = i - 1  # j表示手里最末尾的牌的下标
        while j >= 0 and li[j] > temp:  # 循环的目的就是找到temp要插入的位置
            li[j+1] = li[j]
            j -= 1
        li[j+1] = temp  # while循环结束之后，如果li[j] > temp，li[j]就往右移动一个位置，并且j=j-1，那j这个位置就空了（但是j减小了1），
        # 把temp放在空了这个位置上，这个位置的下标是j+1，因为退出while循环的时候减小了1.
        # print(li)


# li = [random.randint(0, 100) for i in range(10)]
li = list(range(10000))
random.shuffle(li)
# print(li)
# li = select_sort_simple(li)
insert_search(li)
# print(li)
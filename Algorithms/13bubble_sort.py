"""
    冒泡排序
"""
import random


def bubble_sort(li):
    for i in range(len(li)-1):  # 趟数
        for j in range(len(li)-i-1):  # len(li)-i-1无序区域的范围， j表示指针位置
            if li[j] > li[j + 1]:
                li[j], li[j+1] = li[j+1], li[j]
        print(li)


li = [random.randint(0, 100) for i in range(10)]
print(li)
bubble_sort(li)
print(li)
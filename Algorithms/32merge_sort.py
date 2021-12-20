"""
    归并排序
"""


def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <=high:  # 只要两边都有数
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    # while执行完，肯定有一部分没数了
    while i <= mid:  # 右边没有数了，剩下左边
        ltmp.append(li[i])
        i += 1
    while j <= high:  # 左边没有数了，剩下右边
        ltmp.append(li[j])
        j += 1
    li[low:high + 1] = ltmp


# li = [2,4,5,7,1,3,6,8]
# merge(li, 0, 3, 7)
# print(li)


def merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)


# def merge_sort_test(li, low, high):
#     if low < high:
#         mid = (low + high) // 2
#         merge_sort_test(li, low, mid)
#         print(li[low:mid+1])
#         merge_sort_test(li, mid + 1, high)
#         # merge(li, low, mid, high)
#         print(li[mid+1:high + 1])
#         print(li[low:high+1])


li = list(range(100))
import random
random.shuffle(li)
print(li)
merge_sort(li, 0, len(li)-1)
print(li)

"""
    选择排序
"""
import random


def select_sort_simple(li):
    li_new = []  # 空间复杂度 O（n）
    for i in range(len(li)):  # 时间复杂度 O（n）
        min_val = min(li)  # 时间复杂度 O（n）
        li_new.append(min_val)
        li.remove(min_val)  # 时间复杂度 O（n）
    return li_new

def select_sort(li):
    for i in range(len(li)):  # i是第几趟
        min_loc = i
        for j in range(i+1, len(li)):  # 无序区(i+1, len(li))
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
        print(li)


li = [random.randint(0, 100) for i in range(10)]
print(li)
# li = select_sort_simple(li)
select_sort(li)
print(li)



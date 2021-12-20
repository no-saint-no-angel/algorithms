from functools import cmp_to_key
# a = "96"
# b = "87"
#
# a + b if a>b else b + a
#
# a = "128"
# b = "1286"
#
# a+b = "1281286"
# b+a = "1286128"
# a + b if a+b>b+a else b+a

li = [32, 94, 128, 1286, 6, 71, 35, 351, 4]


def xy_cmp(x, y):
    if x+y < y+x:  # 如果成立，说明y在前面，结合之后会更大，需要把x和y换一下顺序
        return 1
    elif x+y > y+x:  # 不用换顺序
        return -1
    else:
        return 0


def bubble_sort(li):
    for i in range(len(li)-1):  # 趟数
        temp_li = li.copy()
        for j in range(len(li)-i-1):  # len(li)-i-1无序区域的范围， j表示指针位置
            if li[j] + li[j + 1] < li[j + 1] + li[j]:   # 如果成立，说明li[j + 1]在前面，结合之后会更大，需要把li[j]和li[j + 1]换一下顺序
                li[j], li[j+1] = li[j+1], li[j]
        if temp_li == li:  # 一般不用排序len(li)-1，就可以完成所有的调整
            break
        print(li)
    return li


def number_join(li):
    li = list(map(str, li))
    li = bubble_sort(li)  # 使用冒泡排序完成排序

    # li = list(map(str, li))  # 将li转换成str
    # li = list(map(str, li))  # 将li转换成str
    # # li = list(map(int, li))  # 将li转换成int
    # # print(li)
    # li.sort(key=cmp_to_key(xy_cmp))  # 这行代码功能是排序。但是具体的排序操作看不懂。如果用冒泡排序的话也可以实现相同的作用。

    return "".join(li)


print(number_join(li))
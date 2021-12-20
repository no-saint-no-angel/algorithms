"""

    快速排序
"""


def partition(li, left, right):
    temp = li[left]
    while left < right:
        while left < right and li[right] >= temp:  # 从右面找比temp小的数
            right -= 1  # 往左走一步
        li[left] = li[right]  # 把右边的值写到左边空位上
        print(li, 'right')
        while left < right and li[left] <= temp:  # 从左面找比temp大的数
            left += 1
        li[right] = li[left]  # 把左边的值写到右边空位上
        print(li, 'left')
    li[left] = temp  # 把tmp归位
    return left


def quick_sort(li, left, right):
    if left<right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid-1)
        quick_sort(li, mid + 1, right)


li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
print(li)
# partition(li, 0, len(li) - 1)
quick_sort(li, 0, len(li) - 1)
print(li)

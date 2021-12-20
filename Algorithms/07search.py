"""
    线性查找和二分查找
"""
# from cal_time import cal_time
#
# @ cal_time
# def linear_search(data_set, value):
#     for i in range(len(data_set)):
#         if data_set[i] == value:
#             return i
#     else:
#         return None
#
#
#
# @ cal_time
# def binary_search(li, val):
#     left = 0
#     right = len(li) - 1
#     while right >= left:
#         mid = (left + right) // 2
#         if li[mid] == val:
#             return mid
#         elif li[mid] > val:
#             right = mid - 1
#         else:
#             left = mid + 1
#     else:
#         return None
#
#
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# binary_search(li, 3580000)
# print()
# li = list(range(100000000))
# print(binary_search(li, 3580000))
# print(linear_search(li, 3580000))

""" 
    1、查找一个有序数列中某个数值的位置
"""
# def binary_search(li, val_num):
#     left = 0
#     right = len(li) - 1
#     while left <= right:
#         mid = (left+right)//2
#         if li[mid] == val_num:
#             return mid
#         elif li[mid] > val_num:
#             right = mid - 1
#         else:
#             left = mid + 1
#     else:
#         return None
#
#
# li = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9]
# print(binary_search(li, 4))

"""
    查找一个有序数列中某个值出现的次数
"""


def binary_search_count(li, val_num):

    def find_right(li, val_num):
        left = 0
        right = len(li) - 1
        while left <= right:
            mid = (left+right)//2
            print('mid', mid)
            if li[mid] > val_num:
                right = mid - 1
            elif li[mid] <= val_num:
                left = mid + 1
        else:
            print('left', right)
            return right
    return find_right(li, val_num) - find_right(li, val_num-1)


li = [1, 2, 3, 4, 4, 4, 4]
print(binary_search_count(li, 4))

# array 二维列表
# 暴力求解
def Find(target, array):
    # write code here
    count = 0
    for i in range(len(array)):
        array_row = array[i]
        if target in array_row:
            count += 1
    if count != 0:
        return True
    else:
        return False


# array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
# print(Find(7, array))

# 二分法求解
class Solution():
    def binary_find(self, target, array):
        row_a = len(array)
        if row_a == 0:
            return False
        clo_a = len(array[1])
        if clo_a == 0:
            return False
        row_val, clo_val = 0, clo_a-1
        while row_val<row_a and clo_val>0:
            if array[row_val][clo_val] == target:
                return True
            elif array[row_val][clo_val] > target:
                clo_val -= 1
            else:
                row_val += 1
        else:
            return False

import numpy as np
array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
s = Solution()
print(s.binary_find(3, array))
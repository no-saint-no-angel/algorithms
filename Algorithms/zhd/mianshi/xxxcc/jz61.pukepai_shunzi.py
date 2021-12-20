
"""

    思路：判断除了0之外有没有重复的数字，如果有重复的，直接返回Flase。
    否则的话，判断除了0之外的数字的最大值和最小值的差DELTE，如果这个差小于5，就可以连成顺子，否则的话，不能连成顺子。
"""

class Solution:
    def isStraight(self, nums) -> bool:
        list_set = set()
        max_nums, min_nums = 0, 14
        for i, num in enumerate(nums):
            if num != 0:
                max_nums = max(num, max_nums)
                min_nums = min(num, min_nums)
            if num in list_set and num != 0:
                return False
            else:
                list_set.add(num)
        return max_nums - min_nums < 5

s = Solution()
list_ = [0, 0, 8, 5, 4]
print(s.isStraight(list_))
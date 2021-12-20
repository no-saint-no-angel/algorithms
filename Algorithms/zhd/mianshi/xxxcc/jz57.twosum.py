
"""

    这里的题目给的是递增排序的数组，所以除了用字典dict或者集合set的方法做，还可以用双指针的方法来做（是一个更优化的方法）
"""
# class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     dic_map = dict()
    #     n = len(nums)
    #     for i, num in enumerate(nums):
    #         tmp = target - num
    #         if tmp in dic_map.keys():
    #             return [tmp, num]
    #         else:
    #             dic_map[num] = i

class Solution:
    def twoSum(self, nums, target):
        # nums.sort()
        l = 0
        r = len(nums) - 1
        while(l < r):
            if (nums[l] + nums[r] < target):
                l += 1
            elif (nums[l] + nums[r] > target):
                r -= 1
            else:
                return [nums[l], nums[r]]
        return []

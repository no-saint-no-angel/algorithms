class Solution:
    def maxSubArray(self, nums):
        tmp = nums[0]
        max_ = tmp
        n = len(nums)
        for i in range(1, n):
            # 当当前序列和（tmp)加上此时的元素(nusm[i])的值大于此时元素的值(nusm[i])，说明最大序列和可能出现在后续序列中，记录此时的最大值
            if tmp + nums[i] > nums[i]:
                max_ = max(max_, tmp + nums[i])
                tmp = tmp + nums[i]
            else:
                # 当当前序列和（tmp)加上此时的元素(nusm[i])的值小于此时元素的值(nusm[i])，当前最长序列到此为止。以该元素为起点继续找最大子序列,
                # 并记录此时的最大值
                max_ = max(max_, tmp, nums[i])
                tmp = nums[i]
        return max_


def max_sub(nums):
    tmp = nums[0]
    max_ = tmp
    n = len(nums)
    for i in range(1, n):
        if tmp > 0:
            max_ = max(max_, tmp)
            tmp += nums[i]
        else:
            max_ = max(max_, tmp)
            tmp = nums[i]
    return max_

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sub(nums))


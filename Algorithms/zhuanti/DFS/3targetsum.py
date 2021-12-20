
class Solution():
    res = 0
    def dfs(self, nums, s, sum, k):
        if k == len(nums):
            if sum == s:
                self.res += 1
                print(self.res)
            return self.res

        self.dfs(nums, s, sum+nums[k], k+1)
        self.dfs(nums, s, sum-nums[k], k+1)

    def findtarget_sum_ways(self, nums, s):

        if nums==None:
            return 0
        else:
            self.dfs(nums, s, 0, 0)
            return self.res


# nums = [47,30,12,40,10,31,5,12,14,25,45,34,34,31,20,1,33,28,30,30]
nums = [1,1,1]
target = 1
s = Solution()
print(s.findtarget_sum_ways(nums, target))
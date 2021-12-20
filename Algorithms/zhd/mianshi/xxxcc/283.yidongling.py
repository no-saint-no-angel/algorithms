class Solution:
    def movezeroes(self, nums):
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        return nums
    def movezeroes_python3(self, nums):  # 不讲五的
        nums_0 = nums.count(0)
        for i in range(nums_0):
            nums.remove(0)  # 这个删除是按照从前往后的顺序来删除
            nums.append(0)
        return nums
    def move0_sort(self, nums):
        return sorted(nums, key= lambda x:x==0, reverse=False)  # 极不讲五的

    def move_0(self, nums):
        left = right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        return nums

s = Solution()
list = [0, 1, 0, 3, 12]
print(s.move_0(list))
class Solution:
    def twosum(self, numbers, target):
        dict_map = dict()
        for i, num in enumerate(numbers):
            temp = target - num
            if temp in dict_map:  # 这个不指明是key还是value的话，默认就是指key。
                return [dict_map[temp] + 1, i+1]
            dict_map[num] = i
            print(dict_map)

    def two_sum(self, nums, target):
        set_map = dict()
        for i in range(len(nums)):
            if target - nums[i] in set_map.keys():
                return [set_map[target - nums[i]]+1, i+1]
            else:
                set_map[nums[i]] = i

    def two_sum_1(self, nums, target):
        set_map = dict()
        for i in range(len(nums)):
            if target - nums[i] in set_map.keys():
                return [set_map[target - nums[i]] + 1, i + 1]
            else:
                set_map[nums[i]] = i


if __name__ == '__main__':
    s = Solution()
    list = [2, 7, 11, 15]
    target = 17
    print(s.two_sum(list, target))
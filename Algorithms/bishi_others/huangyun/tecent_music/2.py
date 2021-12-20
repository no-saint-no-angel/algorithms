class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        list = []
        list_0 = []
        for i in range(n):
            list_0.append(0)
            list.append(int(nums[i]))
        temp = list.copy()
        max_ = list.copy()
        for i in range(1, n):
            if temp[i] == 0:
                for j in range(i, n):
                    max_[i] = 1
                # for k in range(i, j):
                #     list_0[k] = -1
                # temp[i:j] += list_0
                # temp = map(abs, temp)
                #
                # if ''.join(temp) > ''.join(max_):
                #     max_ = temp
                # else:
                #     max_ = max_
        return ''.join(map(str, max_))
        # return max_

if __name__ == '__main__':
    s = Solution()
    a = '100101'
    print(s.maxSubArray(a))

    a = [1, 2, 3]
    for i in range(2,3):
        print(a[i])
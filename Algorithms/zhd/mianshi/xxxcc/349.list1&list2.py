"""
    这个题目只要求两个数组相同的数字，而且重复的数字只要写一个就行，并对位置不做要求(这个方法不会改变位置）
    所以直接用set()内置的方法来做
"""

class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1)&set(nums2))


if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [2, 2, 4, 7]
    s = Solution()
    print(s.intersection(list1, list2))

"""
    转成集合，然后用集合内置的取交集函数完成
"""

"""
    时间复杂度：set()取交集的时间复杂度是O(m+n)
    空间复杂度：O(m+n)    %这种怎么算空间复杂度
"""
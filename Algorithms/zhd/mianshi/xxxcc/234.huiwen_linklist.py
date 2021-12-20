
"""
    思路：
    先遍历链表，把值存储在列表中，然后再对列表判断是否是回文数字。可以调用列表的revsersed函数，实现列表反转
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        str_list = list()
        while head:
            str_list.append(head.val)
            head = head.next
        return str_list == list(reversed(str_list))

"""
时间复杂度：O(n)，其中 n 指的是链表的元素个数。
第一步： 遍历链表并将值复制到数组中，O(n)。
第二步：双指针判断是否为回文，执行了 O(n/2) 次的判断，O(n)。
总的时间复杂度：O(2n) = O(n)O(2n)=O(n)。
空间复杂度：O(n)，其中 n 指的是链表的元素个数，我们使用了一个数组列表存放链表的元素值。

"""
"""
    题目：
    输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
    思路：
    返回的也是一个链表，只不过他的长度是K，返回值是这个长度为k的链表的head。问题就变成了怎么求这个链表的头节点的位置。
    直接的思路就是，用输入链表的长度减去K得到差值A，然后对输入链表循环A次，就得到我们想要的（长度为k的链表的head）
    而链表的长度就是先遍历一遍输入，用列表来存储链表节点值，然后就得到链表长度。

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        list_link = list()
        cur = head
        while cur:
            list_link.append(cur.val)
            cur = cur.next
        for i in range(len(list_link)-k):
            head = head.next
        return head


"""
    思路2：用双指针的方法，
    定义两个指针，former,latter。先让former指针先走k个节点，然后再让两个节点同时遍历整个链表，直到前面的指针former走到头（null)，
    此时latter的位置就是我们要输出的链表的头节点。
    
    算法流程：
        1、初始化： 前指针 former 、后指针 latter ，双指针都指向头节点 head​ 。
        2、构建双指针距离： 前指针 former 先向前走 kk 步（结束后，双指针 former 和 latter 间相距 kk 步）。
        3、双指针共同移动： 循环中，双指针 former 和 latter 每轮都向前走一步，直至 former 走过链表 尾节点 时跳出（跳出后， latter 与尾节点距离为 k-1k−1，即 latter 指向倒数第 kk 个节点）。
        4、返回值： 返回 latter 即可。

"""
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former, latter = head, head
        for _ in range(k):
            if not former: return
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter

"""
时间复杂度 O(N) ：N 为链表长度；总体看， former 走了 N 步， latter 走了 (N−k) 步。
空间复杂度 O(1) ： 双指针 former , latter 使用常数大小的额外空间。

"""

"""

    思路 :
    我们使用两个指针 node1，node2 分别指向两个链表 headA，headB 的头结点，然后同时分别逐结点遍历，
    当 node1 到达链表 headA 的末尾时，重新定位到链表 headB 的头结点；当 node2 到达链表 headB 的末尾时，
    重新定位到链表 headA 的头结点。

    这样，当它们相遇时，所指向的结点就是第一个公共结点。
    朴素理解：
    headA和headB的长度可以分别看作len_A+C和len_B+C，即各自的非重叠部分和重叠部分C，比如链表A，当遍历完len_A+C
    之后，链表重新定位到链表B的头节点，继续遍历len_B。同理链表B遍历结束之后定位到链表A头节点，继续遍历len_A。
    最终遍历相同的长度len_A+len_B+C，到达相遇的节点。
    对于没有交点的两个链表，遍历len_A+len_B的长度，最后两个节点同时为null，退出循环，返回null。
    对于没有交点的两个链表，遍历len_A+len_B的长度，最后两个节点同时为null，退出循环，返回null。
"""


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB

        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1

"""
- 时间复杂度：O(M+N)。
- 空间复杂度：O(1)。
"""


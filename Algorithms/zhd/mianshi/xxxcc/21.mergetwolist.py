
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkList(object):
    def __init__(self):
        self.head = None

    # 链表初始化函数, 方法类似于尾插
    def initList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return self.head

    # 链表判空
    def isEmpty(self):
        if self.head.next == 0:
            print("Empty List!")

            return 1
        else:
            return 0

    def traveList(self):
        if self.isEmpty():
            exit(0)
        print('\rlink list traving result: ', )
        p = self.head
        while p:
            print(p.val)
            p = p.next

"""

终止条件：当两个链表都为空时，表示我们对链表已合并完成。
如何递归：我们判断 l1 和 l2 头结点哪个更小，然后较小结点的 next 指针指向其余结点的合并结果。（调用递归）
        其余结果的合并方式也是一样的，继续判断l1 和 l2 头结点哪个更小，然后较小结点的 next 指针指向其余结点的合并结果。
        这样就可以通过递归来实现

"""

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2  # 终止条件，直到两个链表都空
        if not l2: return l1
        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2

"""
时间复杂度：O(m+n).递归函数每次去掉一个元素，直到两个链表都为空，因此需要调用 R=O(m+n) 次。
而在递归函数中我们只进行了 next 指针的赋值操作，复杂度为O(1)，故递归的总时间复杂度为R∗O(1)=O(m+n) 。

空间复杂度：O(m+n)。对于递归调用 self.mergeTwoLists()，当它遇到终止条件准备回溯时，已经递归调用m+n 次，
使用了m+n 个栈帧，故最后的空间复杂度为O(m+n)
"""

if __name__ == '__main__':
    head1 = [1, 2, 3, 4, 5]
    head2 = [2,3,9]
    listlink = LinkList()
    head_list_1 = listlink.initList(head1)
    head_list_2 = listlink.initList(head2)
    s = Solution()
    merge_12 = s.mergeTwoLists(head_list_1, head_list_2)

    # 打印合并之后的list
    list_merge_12 = list()
    while merge_12:
        # print(merge_12.val)
        list_merge_12.append(merge_12.val)
        merge_12 = merge_12.next
    print(list_merge_12)


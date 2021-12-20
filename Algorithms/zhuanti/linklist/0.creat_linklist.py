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


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    listlink = LinkList()
    head_list = listlink.initList(head)
    listlink.traveList()
    print(head_list)


"""

    这是一个很通用的层序遍历的方法，其他类似的层序遍历变种题目都可以套用这个方法。
    比如：103，107，199
    思路：
    1、如果是空子树，直接返回[]
        if not root: return []
    2、首先根据节点入队列queue，queue表示当前层的节点，开始遍历
        queue = [root]
        res = []
        while queue:
    3、把当前层queue的节点的值入队列
        res.append([node.val for node in queue])
    4、遍历当前层queue的每个结点的左子结点，右子结点，入队列，最关键的地方是：把queue列表更新成当前层的孩子节点列表,直到queue为空
        #存储当前层的孩子节点列表
        ll = []
        for node in queue:
            #如果左子节点存在，入队列
            if node.left:
                ll.append(node.left)
            #如果右子节点存在，入队列
            if node.right:
                ll.append(node.right)
        #遍历列表更新为孩子节点列表
        queue = ll
    5、返回res

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinTree():
    def __init__(self):
        self.root = None
        self.ls = []

    def add(self, data):
        node = TreeNode(data)
        if self.root == None:
            self.root = node
            self.ls.append(self.root)
        else:
            rootNode = self.ls[0]
            if rootNode.left == None:
                rootNode.left = node
                self.ls.append(rootNode.left)
            elif rootNode.right == None:
                rootNode.right = node
                self.ls.append(rootNode.right)
                self.ls.pop(0)


class Solution:
    def levelOrder(self, root):
        if not root: return []
        #跟结点入queue
        queue = [root]
        res = []
        while queue:
            res.append([node.val for node in queue])
            #存储当前层的孩子节点列表
            ll = []
            #对当前层的每个节点遍历
            for node in queue:
                #如果左子节点存在，入队列
                if node.left:
                    ll.append(node.left)
                #如果右子节点存在，入队列
                if node.right:
                    ll.append(node.right)
            #后把queue更新成下一层的结点，继续遍历下一层
            queue = ll
        return res

if __name__ == '__main__':
    tree = BinTree()
    for i in range(1, 11):
        tree.add(i)
    s = Solution()
    print(s.levelOrder(tree.root))

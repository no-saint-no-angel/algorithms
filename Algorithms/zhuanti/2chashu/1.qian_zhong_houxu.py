"""

    二叉树的前序，中序，后续遍历有两类方式，一类是用递归，一类是迭代
    用递归会简单很多，迭代复杂一点
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



class Solution_qzh:
    def preorderTraversal(self, root):

        def pt(root):
            if not root:
                return dict_map
            dict_map.append(root.val)
            if root.left:
                pt(root.left)
            if root.right:
                pt(root.right)
        dict_map = list()
        pt(root)
        return dict_map

    def inorderTraversal(self, root):
        dict_map = list()
        def it(root):
            if not root:
                return dict_map
            if root.left:
                it(root.left)
            dict_map.append(root.val)
            if root.right:
                it(root.right)
        it(root)
        return dict_map

    def postorderTraversal(self, root):
        dict_map = list()
        def pt(root):
            if not root:
                return dict_map
            if root.left:
                pt(root.left)
            if root.right:
                pt(root.right)
            dict_map.append(root.val)
        pt(root)
        return dict_map


if __name__ == '__main__':
    tree = BinTree()
    for i in range(1, 11):
        tree.add(i)
    s = Solution_qzh()
    print(s.postorderTraversal(tree.root))


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

if __name__ == '__main__':
    tree = BinTree()
    for i in range(1, 11):
        tree.add(i)
    print(1)

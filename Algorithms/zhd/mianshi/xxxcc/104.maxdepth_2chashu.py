
"""

    思路：二叉树的最大深度可以分解为，先求左右两个子树的深度，比较得到更深的那一棵，再加上一就是二叉树的最大深度
    而左子树和右子树又可以用同样的方式来计算。因此可以用深度优先搜索的方法来计算二叉树的最大深度。
    具体而言：在计算当前二叉树的最大深度时，可以先递归计算出其左子树和右子树的最大深度，
    然后在 O(1)时间内计算出当前二叉树的最大深度。递归在访问到空节点时退出。

"""
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

"""
时间复杂度：O(n)，其中 nn 为二叉树节点的个数。每个节点在递归中只被遍历一次。

空间复杂度：O(height) 表示二叉树的高度。递归函数需要栈空间，而栈空间取决于递归的深度，因此空间复杂度等价于二叉树的高度。

"""
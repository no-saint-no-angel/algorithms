
"""

    这个思路是，求N叉树的最大深度，可以拆解为一个子问题，求所有根节点子树的最大深度，比较得到最深的那一棵，
    加上1就是N叉树的最大深度，而子树的最大深度又可以用同样的方式来计算。因此可以用深度优先搜索的方式来计算N叉树的最大深度
    递归终止条件是：子树是否为空
    遍历每个节点，直到叶子节点开始返回
    具体而言：在计算当前N叉树的最大深度时，可以先递归计算出其所有子树的最大深度，
    然后在 O(1)时间内计算出当前N叉树的最大深度。递归在访问到空节点时退出。
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        elif root.children == []:
            return 1
        else:
            height = [self.maxDepth(c) for c in root.children]
            return max(height) + 1
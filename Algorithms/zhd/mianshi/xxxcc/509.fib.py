"""
    这里用三种方法来解决斐波那契数列求和
    一是递归
    二是带备忘录的递归
    三是动态规划方法
    四是优化的动态规划方法
"""


class Solution:
    """
        1、递归
    """
    def fib_1(self, n):
        if n == 1 or n == 2:
            return 1
        return self.fib_1(n-1)+self.fib_1(n-2)

    """
        2、带备忘录的递归(自顶向下）
    """
    def fib_2(self, n):
        memo = [0 for _ in range(n+1)]
        return self.helper(memo, n)

    def helper(self, memo, n):
        if n == 1 or n == 2:
            return 1
        # 判断是否已经计算过，如果计算过，直接返回，否则计算
        if memo[n] != 0:
            return memo[n]
        else:
            memo[n] = self.helper(memo, n-1) + self.helper(memo, n-2)
        return memo[n]

    """
        3、动态规划（自底向上）
    """
    def fib_3(self, n):
        dp = [0 for _ in range(n + 1)]
        dp[1] = dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    """
        4、动态规划优化版本，其实斐波那契数列只要存储三个位置的数，当前状态需要计算的数，当前状态前面两个状态的数
    """
    def fib_4(self, n):
        pre, cur, next = 0, 1, 1
        for i in range(n):
            next = pre + cur
            pre = cur
            cur = next
        return pre

if __name__ == '__main__':
    num = 45
    s = Solution()
    print(s.fib_4(num))



"""

    这个青蛙跳台阶问题第一次看了看不懂，看解析也是。
    第二次看解析说可以转化为斐波那契数列问题，我就试着把前几种情况列出来，发现还真是斐波那契数列，就直接用滚动数组做了。
"""


class Solution:
    # 递归
    def climbStairs_digui(self, n):
        if n==0 or n==1:
            return 1
        return self.climbStairs_digui(n-1) + self.climbStairs_digui(n-2)

    # 带记忆的递归，自顶向下
    def climbStairs_jiyi(self, n):
        def dfs(i, memo):
            if i == 0 or i==1:
                return 1
            if memo[i] == -1:
                memo[i] = dfs(n-1, memo) + dfs(n-2, memo)
            return memo
        return dfs(n, [-1]*(n+1))  # 初始化一个全为-1的memo

    # 自底向上dp，这个看起来也不难理解，但是很难想得到
    def climbStairs_dp(self, n):
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        pre, cur, post = 1, 2, 3
        for i in range(1, n):
            post = pre + cur
            pre = cur
            cur = post
        return pre


if __name__ == '__main__':
    s = Solution()
    print(int(s.climbStairs_dp(78)%(1e9+7)))

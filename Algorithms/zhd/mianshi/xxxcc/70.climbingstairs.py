

"""
    暴力深度优先搜索
"""

def clbs(n):
    if n == 0 or n == 1:
        return 1
    return clbs(n-1) + clbs(n-2)

"""
    这个记忆化递归没理解
"""
# 记忆化递归，自顶向下
def clbs_memo(n):
    def dfs(i: int, memo) -> int:
        if i == 0 or i == 1:
            return 1
        if memo[i] == -1:
            memo[i] = dfs(i - 1, memo) + dfs(i - 2, memo)
        return memo[i]

    # memo: [-1] * (n - 1)
    # -1 表示没有计算过，最大索引为 n，因此数组大小需要 n + 1
    return dfs(n, [-1] * (n + 1))

# https://leetcode-cn.com/problems/climbing-stairs/solution/zhi-xin-hua-shi-pa-lou-ti-zhi-cong-bao-l-lo1t/

if __name__ == '__main__':
    n = 20
    print(clbs_memo(n))
    # enumerate
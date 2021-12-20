class Solution:
    # def coinChange(coins: List[int], amount: int):

    #     def dp(n):
    #         # base case
    #         if n == 0: return 0
    #         if n < 0: return -1
    #         # 求最小值，所以初始化为正无穷
    #         res = float('INF')
    #         for coin in coins:
    #             subproblem = dp(n - coin)
    #             # 子问题无解，跳过
    #             if subproblem == -1: continue
    #             res = min(res, 1 + subproblem)

    #         return res if res != float('INF') else -1

    #     return dp(amount)
    def coinChange(self, coins, amount):
        # 备忘录
        memo = dict()

        def dp(n):
            # 查备忘录，避免重复计算
            if n in memo: return memo[n]
            # base case
            if n == 0: return 0
            if n < 0: return -1
            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1: continue
                res = min(res, 1 + subproblem)

            # 记入备忘录
            memo[n] = res if res != float('INF') else -1
            return memo[n]

        return dp(amount)


if __name__ == '__main__':
    coins = [1, 2, 5]
    count = 100
    s = Solution()
    print(s.coinChange(coins, count))

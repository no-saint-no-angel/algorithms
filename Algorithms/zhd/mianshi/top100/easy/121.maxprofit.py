


class Solution:
    """
        第一种是自己的想法：分析了各种情况，有十几个用例每过。
        没过的，就是针对从高降低的情况，最大点在前面，下降，在升高，再下降，再升高，再下降。。。。。。
        这种情况根本不好分类来解决。所以放弃
    """
    def maxProfit_myself(self, prices) -> int:
        max_l = max(prices)
        min_l = min(prices)

        if prices.index(min_l) < prices.index(max_l):
            return max_l - min_l
        else:
            min_l_pre = min(prices[0:prices.index(max_l)+1])
            max_l_post = max(prices[prices.index(min_l):])

            if max_l-min_l_pre>max_l_post-min_l:
                return max_l-min_l_pre
            else:
                return max_l_post-min_l
    """
        这种方法是，官方的
        用两个变量存放当前最大利润max_和历史最小值min_（当前历史最小值）
        流程：
        循环遍历每个值
        当前值减去min_，得到当前可能最大利润值，然后比较其与max_的大小，更新max_
        比较当前值和min_，更新min_
        返回最大利润
        
    """
    def maxProfit_offi(self, prices) -> int:
        max_ = 0
        min_ = int(1e9)
        for price in prices:
            max_ = max(max_, price-min_)
            min_ = min(min_, price)
        return max_


if __name__ == '__main__':
    # prices = [7, 1, 5, 3, 6, 4]
    prices = [7,2,4,1]
    s = Solution()
    print(s.maxProfit(prices))
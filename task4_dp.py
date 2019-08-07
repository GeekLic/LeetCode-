"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        K = 2
        if n <= 1:
            return 0
        dp = [[[0] * 2 for j in range(K+1)] for i in range(n)]
        for i in range(n):
            """处理base case"""
            if i - 1 == -1:
                for k in range(K+1):
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                continue
            for k in range(1,K+1):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[n-1][K][0]
"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""
# class Graph(object):
#     def __init__(self,lists):
#         self._val = lists
#         n = len(lists)
#         self._next = [[0]*n for i in range(n)]
#         for j in range(1, n):
#             for i in range(j):
#                 if lists[j] > lists[i]:
#                     minus = lists[j] - lists[i]
#                     self._next[j][i] = minus
#
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         G = Graph(prices)
#         n = len(G._val)
#         if n <= 1:
#             return 0
#         distance = [0] * n
#         for i in range(1, n):
#             cur = G._next[i]
#             for j in range(i):
#                 cur[j] += distance[j]
#             distance[i] = max(cur)
#         return max(distance)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                maxprofit += prices[i] - prices[i - 1]
        return maxprofit
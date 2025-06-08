from typing import List


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         res = 0
#         for i in range(len(prices)-1):
#             if prices[i] < prices[i+1]:
#                 res += prices[i+1] - prices[i]
#         return res



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = 0            # 第0天，手上無持有狀態
        dp[0][1] = -prices[0]   # 第0天，手上有持有狀態
        for i in range(1, n):
            dp[i][0] = max(prices[i] + dp[i-1][1], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])

        return dp[n-1][0]

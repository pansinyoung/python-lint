"""
151. Best Time to Buy and Sell Stock III
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Example
Example 1

Input : [4,4,6,1,1,4,2,5]
Output : 6
Notice
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution:
    def maxProfit(self, prices):
        if not prices or len(prices) <= 1:
            return 0
        n = len(prices)
        p1 = [0 for _ in prices]
        p2 = [0 for _ in prices]
        min_price = prices[0]
        for i in range(1, n):
            p1[i] = max(prices[i] - min_price, p1[i-1])
            min_price = min(min_price, prices[i])
        max_price = prices[n - 1]
        for i in range(n - 2, -1, -1):
            p2[i] = max(max_price - prices[i], p2[i + 1])
            max_price = max(max_price, prices[i])
        return max([p1[i] + p2[i] for i in range(n)])
#!/usr/bin/python
"""https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price, max_profit = float('inf'), 0
        for price in prices:
            min_price = price if price < min_price else min_price
            profit_temp = price - min_price
            max_profit = profit_temp if profit_temp > max_profit else max_profit
        return max_profit

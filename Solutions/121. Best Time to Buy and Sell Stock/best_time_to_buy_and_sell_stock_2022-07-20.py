#!/usr/bin/env python3
"""https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price, max_profit = float('inf'), 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

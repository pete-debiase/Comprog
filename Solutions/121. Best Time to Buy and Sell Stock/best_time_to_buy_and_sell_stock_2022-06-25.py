#!/usr/bin/env python3
"""https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        price_min, profit_max = float('inf'), 0
        for price in prices:
            price_min = min(price_min, price)
            profit_max = max(profit_max, price - price_min)
        return profit_max

#!/usr/bin/python
"""https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"""

import timeit

class SolutionInitial:
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            current_price = prices[i]
            future_prices = prices[i + 1:]
            max_future_price = max(future_prices)
            if max_future_price > current_price:
                max_profit_temp = max_future_price - current_price
                max_profit = max_profit_temp if max_profit_temp > max_profit else max_profit
        return max_profit

class SolutionPreferred():
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfit(self, prices: list[int]) -> int:
        min_price, max_profit = float('inf'), 0
        for price in prices:
            min_price = price if price < min_price else min_price
            profit_temp = price - min_price
            max_profit = profit_temp if profit_temp > max_profit else max_profit
        return max_profit


if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_preferred = SolutionPreferred()

    # Example 1 (Expected Output: 5)
    prices = [7, 1, 5, 3, 6, 4]
    print(solution_initial.maxProfit(prices))
    print(solution_preferred.maxProfit(prices))

    # Example 2 (Expected Output: 0)
    prices = [7, 6, 4, 3, 1]
    print(solution_initial.maxProfit(prices))
    print(solution_preferred.maxProfit(prices))

    # Benchmarking
    prices = list(range(1000))
    print(timeit.timeit(lambda: solution_initial.maxProfit(prices), number=1000))
    print(timeit.timeit(lambda: solution_preferred.maxProfit(prices), number=1000))

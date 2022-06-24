#!/usr/bin/env python3
"""https://leetcode.com/problems/maximum-product-subarray/"""

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        min_temp, max_temp, max_final = 1, 1, -float('inf')
        for n in nums:
            x = min_temp * n
            y = max_temp * n
            min_temp = min(n, x, y)
            max_temp = max(n, x, y)
            max_final = max(max_final, max_temp)
        return max_final

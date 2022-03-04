#!/usr/bin/python
"""https://leetcode.com/problems/maximum-product-subarray/"""

class Solution:
    def maxProduct(self, numbers: list[int]) -> int:
        max_current, min_current, max_final = 1, 1, -float('inf')
        for n in numbers:
            x = max_current * n
            y = min_current * n
            min_current = min(n, x, y)
            max_current = max(n, x, y)
            max_final = max(max_current, max_final)
        return max_final

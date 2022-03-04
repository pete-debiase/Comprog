#!/usr/bin/python
"""https://leetcode.com/problems/maximum-product-subarray/"""

class Solution:
    def maxProduct(self, numbers: list[int]) -> int:
        product_current, product_max, product_neg = 1, -float('inf'), float('inf')
        for number in numbers:
            product_current = max(number, product_current * number)
            product_neg = min(product_neg, product_neg * number)
            product_max = max(product_current, product_max, product_neg)
        return product_max



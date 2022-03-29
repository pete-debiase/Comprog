#!/usr/bin/env python3
"""https://leetcode.com/problems/product-of-array-except-self/"""

class Solution:
    def productExceptSelf(self, numbers: list[int]) -> list[int]:
        n = len(numbers)
        products = [0] * n

        products[0] = 1
        for i in range(1, n):
            products[i] = products[i - 1] * numbers[i - 1]

        product_right = 1
        for i in reversed(range(n)):
            products[i] *= product_right
            product_right *= numbers[i]

        return products

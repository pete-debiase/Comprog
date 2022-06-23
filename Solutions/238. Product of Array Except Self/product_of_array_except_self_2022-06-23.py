#!/usr/bin/env python3
"""https://leetcode.com/problems/product-of-array-except-self/"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        products = [0] * n

        products[0] = 1
        for i in range(1, n):
            products[i] = products[i - 1] * nums[i - 1]

        right_product = 1
        for i in reversed(range(n)):
            products[i] *= right_product
            right_product *= nums[i]

        return products

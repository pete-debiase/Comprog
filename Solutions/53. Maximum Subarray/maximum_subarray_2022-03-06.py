#!/usr/bin/env python3
"""https://leetcode.com/problems/maximum-subarray/"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sum_temp, sum_max = 0, -float('inf')
        for n in nums:
            sum_temp = max(n, n + sum_temp)
            sum_max = max(sum_max, sum_temp)
        return sum_max

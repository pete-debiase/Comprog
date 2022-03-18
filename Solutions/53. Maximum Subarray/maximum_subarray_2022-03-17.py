#!/usr/bin/python
"""https://leetcode.com/problems/maximum-subarray/"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sum_current, sum_max = 0, -float('inf')
        for n in nums:
            sum_current = max(n, sum_current + n)
            sum_max = max(sum_max, sum_current)
        return sum_max

#!/usr/bin/python
"""https://leetcode.com/problems/maximum-subarray/"""

class Solution:
    def maxSubArray(self, numbers: list[int]) -> int:
        sum_current, sum_max = 0, -float('inf')
        for number in numbers:
            sum_current = max(number, sum_current + number)
            sum_max = max(sum_current, sum_max)
        return sum_max

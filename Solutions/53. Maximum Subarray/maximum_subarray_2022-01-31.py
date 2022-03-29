#!/usr/bin/env python3
"""https://leetcode.com/problems/maximum-subarray/"""

class Solution:
    def maxSubArray(self, numbers: list[int]) -> int:
        sum_max = sum_current = numbers[0]
        for number in numbers[1:]:
            sum_current = max(number, sum_current + number)
            sum_max = max(sum_current, sum_max)
        return sum_max

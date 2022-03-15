#!/usr/bin/python
"""https://leetcode.com/problems/maximum-subarray/"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sum_temp, sum_max = 0, -float('inf')
        for num in nums:
            sum_temp = max(num, sum_temp + num)
            sum_max = max(sum_max, sum_temp)
        return sum_max

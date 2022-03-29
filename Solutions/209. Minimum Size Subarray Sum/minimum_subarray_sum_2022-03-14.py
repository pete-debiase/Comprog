#!/usr/bin/env python3
"""https://leetcode.com/problems/minimum-size-subarray-sum/"""

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        i, total, length_min = 0, 0, n + 1
        for j in range(n):
            total += nums[j]
            while total >= target:
                length_min = min(length_min, j - i + 1)
                total -= nums[i]
                i += 1
        return length_min if length_min <= n else 0

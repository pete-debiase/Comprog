#!/usr/bin/env python3
"""https://leetcode.com/problems/minimum-size-subarray-sum/"""

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        l, total, min_length = 0, 0, n + 1
        for r in range(n):
            total += nums[r]
            while total >= target:
                min_length = min(min_length, r - l + 1)
                total -= nums[l]
                l += 1
        return min_length if min_length <= n else 0

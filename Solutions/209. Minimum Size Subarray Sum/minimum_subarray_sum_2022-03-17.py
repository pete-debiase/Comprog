#!/usr/bin/python
"""https://leetcode.com/problems/minimum-size-subarray-sum/"""

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        l, total, length_min = 0, 0, n + 1
        for r in range(n):
            total += nums[r]
            while total >= target:
                length_min = min(length_min, r - l + 1)
                total -= nums[l]
                l += 1
        return length_min if length_min <= n else 0

#!/usr/bin/env python3
"""https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            sum_temp = nums[l] + nums[r]
            if sum_temp == target: return [l + 1, r + 1]
            elif sum_temp < target: l += 1
            elif sum_temp > target: r -= 1
        return []

#!/usr/bin/env python3
"""https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            sum_temp = nums[left] + nums[right]
            if sum_temp == target:
                return [left + 1, right + 1]
            elif sum_temp < target:
                left += 1
            else:
                right -= 1
        return []

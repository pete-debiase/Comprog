#!/usr/bin/env python3
"""https://leetcode.com/problems/sort-colors/"""

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        p0, i, p2 = 0, 0, len(nums) - 1
        while i <= p2:
            if nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                p0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            else:
                i += 1

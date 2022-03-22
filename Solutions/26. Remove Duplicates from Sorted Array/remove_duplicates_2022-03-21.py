#!/usr/bin/python
"""https://leetcode.com/problems/remove-duplicates-from-sorted-array/"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
        return l + 1

#!/usr/bin/env python3
"""https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/"""

class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        lo, hi = 0, n - 1
        if n == 1 or nums[lo] < nums[hi]:
            return nums[lo]

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < nums[lo]:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1

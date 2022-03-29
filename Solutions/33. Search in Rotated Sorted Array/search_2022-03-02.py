#!/usr/bin/env python3
"""https://leetcode.com/problems/search-in-rotated-sorted-array/"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[lo]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1

    def find_rotation_index(self, nums: list[int]) -> int:
        n = len(nums)
        lo, hi = 0, n - 1
        if n == 1: return 0
        if nums[lo] < nums[hi]: return 0

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[mid + 1]:
                return mid + 1
            else:
                if nums[mid] < nums[lo]:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return -1

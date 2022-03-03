#!/usr/bin/python
"""https://leetcode.com/problems/search-in-rotated-sorted-array/"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i_lo, i_hi = 0, len(nums) - 1
        while i_lo <= i_hi:
            i_mid = (i_lo + i_hi) // 2
            if nums[i_mid] == target:
                return i_mid
            elif nums[i_mid] >= nums[i_lo]:
                if nums[i_lo] <= target < nums[i_mid]:
                    i_hi = i_mid - 1
                else:
                    i_lo = i_mid + 1
            else:
                if nums[i_mid] < target <= nums[i_hi]:
                    i_lo = i_mid + 1
                else:
                    i_hi = i_mid - 1
        return -1

    def find_rotation_index(self, nums: list[int]) -> int:
        n = len(nums)
        i_lo, i_hi = 0, n - 1
        if n == 1: return 0
        if nums[i_lo] < nums[i_hi]: return 0

        while i_lo <= i_hi:
            i_mid = (i_lo + i_hi) // 2
            if nums[i_mid] > nums[i_mid + 1]:
                return i_mid + 1
            else:
                if nums[i_mid] < nums[i_lo]:
                    i_hi = i_mid - 1
                else:
                    i_lo = i_mid + 1
        return -1

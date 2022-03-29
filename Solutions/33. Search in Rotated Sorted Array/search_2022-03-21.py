#!/usr/bin/env python3
"""https://leetcode.com/problems/search-in-rotated-sorted-array/"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target: return m
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

    def find_rotation_index(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        if n == 1 or nums[l] < nums[r]: return 0

        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[m + 1]: return m + 1
            elif nums[m] < nums[l]:
                r = m - 1
            else:
                l = m + 1

#!/usr/bin/env python3
"""https://leetcode.com/problems/search-in-rotated-sorted-array/"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    def find_rotation_index(self, nums):
        n = len(nums)
        left, right = 0, n - 1
        if n == 1 or nums[left] < nums[right]: return 0

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return mid + 1
            elif nums[left] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1


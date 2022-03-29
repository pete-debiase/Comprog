#!/usr/bin/env python3
"""https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/"""

class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        if n == 1 or nums[left] < nums[right]: return nums[left]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]: return nums[mid + 1]
            elif nums[left] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

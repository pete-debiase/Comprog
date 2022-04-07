#!/usr/bin/env python3
"""https://leetcode.com/problems/max-consecutive-ones-iii/"""

class SolutionRough:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = zeros = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            if zeros > k:
                if nums[l] == 0: zeros -= 1
                l += 1
        return r - l + 1

class SolutionCleaner:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = 0
        for r in range(len(nums)):
            k -= 1 - nums[r]
            if k < 0:
                k += 1 - nums[l]
                l += 1
        return r - l + 1

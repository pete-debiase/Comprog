#!/usr/bin/env python3
"""https://leetcode.com/problems/3sum/"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0: break
            elif i == 0 or nums[i] != nums[i - 1]:
                self._two_sum(nums, i, triplets)
        return triplets

    def _two_sum(self, nums: list[int], i: int, triplets: list[list[int]]):
        l, r = i + 1, len(nums) - 1
        while l < r:
            triplet = [nums[i], nums[l], nums[r]]
            total = sum(triplet)
            if total < 0: l += 1
            elif total > 0: r -= 1
            else:
                triplets.append(triplet)
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1

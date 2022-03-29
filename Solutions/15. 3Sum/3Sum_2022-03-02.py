#!/usr/bin/env python3
"""https://leetcode.com/problems/3sum/"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0: break
            elif i == 0 or nums[i] != nums[i - 1]:
                self.two_sum(nums, i, triplets)
        return triplets

    def two_sum(self, nums: list[int], i: int, triplets: list[list[int]]):
        i_lo, i_hi = i + 1, len(nums) - 1
        while i_lo < i_hi:
            triplet = [nums[i], nums[i_lo], nums[i_hi]]
            sum_temp = sum(triplet)
            if sum_temp < 0: i_lo += 1
            elif sum_temp > 0: i_hi -= 1
            else:
                triplets.append(triplet)
                i_lo, i_hi = i_lo + 1, i_hi - 1
                while i_lo < i_hi and nums[i_lo] == nums[i_lo - 1]:
                    i_lo += 1

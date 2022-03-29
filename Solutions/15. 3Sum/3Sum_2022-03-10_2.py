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
        left, right = i + 1, len(nums) - 1
        while left < right:
            triplet = [nums[i], nums[left], nums[right]]
            sum_temp = sum(triplet)
            if sum_temp < 0: left += 1
            elif sum_temp > 0: right -= 1
            else:
                triplets.append(triplet)
                left, right = left + 1, right - 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

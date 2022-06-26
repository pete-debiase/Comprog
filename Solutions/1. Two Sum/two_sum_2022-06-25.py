#!/usr/bin/env python3
"""https://leetcode.com/problems/two-sum/"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[n] = i

#!/usr/bin/env python3
"""https://leetcode.com/problems/two-sum/"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, n in enumerate(numbers):
            complement = target - n
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[n] = i

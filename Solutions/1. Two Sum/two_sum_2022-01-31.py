#!/usr/bin/python
"""https://leetcode.com/problems/two-sum/"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, number in enumerate(numbers):
            complement = target - number
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[number] = i

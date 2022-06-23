#!/usr/bin/env python3
"""https://leetcode.com/problems/contains-duplicate/"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return True
            hashmap[num] = 'seen'
        return False

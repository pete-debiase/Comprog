#!/usr/bin/env python3
"""https://leetcode.com/problems/contains-duplicate/"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        len_list = len(nums)
        len_set = len(set(nums))
        return len_list > len_set

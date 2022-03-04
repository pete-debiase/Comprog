#!/usr/bin/python
"""https://leetcode.com/problems/contains-duplicate/"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        length_list = len(nums)
        length_set = len(set(nums))
        return length_list > length_set


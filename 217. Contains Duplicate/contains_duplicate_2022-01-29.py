#!/usr/bin/python
"""https://leetcode.com/problems/contains-duplicate/"""

class Solution:
    def containsDuplicate(self, numbers: list[int]) -> bool:
        length_list = len(numbers)
        length_set = len(set(numbers))
        return length_list > length_set

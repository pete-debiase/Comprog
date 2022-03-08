#!/usr/bin/python
"""https://leetcode.com/problems/valid-parentheses/solution/"""

class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        left = length_max = dirty = 0
        indexes = {}
        for right, c in enumerate(string):
            if c in indexes and left <= indexes[c]:
                left = indexes[c] + 1
            else:
                length_max = max(length_max, right - left + 1)
                if length_max != dirty:
                    dirty = length_max
                    substring = string[left:right + 1]
            indexes[c] = right
        return length_max

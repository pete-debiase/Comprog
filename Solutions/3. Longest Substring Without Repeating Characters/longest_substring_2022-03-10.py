#!/usr/bin/env python3
"""https://leetcode.com/problems/longest-substring-without-repeating-characters/"""

class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        indexes = {}
        length_max = left = 0
        for right, c in enumerate(string):
            if c in indexes and left <= indexes[c]:
                left = indexes[c] + 1
            else:
                length_max = max(length_max, right - left + 1)
            indexes[c] = right
        return length_max

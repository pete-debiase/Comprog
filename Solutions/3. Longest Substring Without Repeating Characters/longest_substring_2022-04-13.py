#!/usr/bin/env python3
"""https://leetcode.com/problems/longest-substring-without-repeating-characters/"""

class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        prev_use_indices = {}
        l = max_length = 0
        for r, c in enumerate(string):
            if c in prev_use_indices and prev_use_indices[c] >= l:
                l = prev_use_indices[c] + 1
            else:
                max_length = max(max_length, r - l + 1)
            prev_use_indices[c] = r
        return max_length

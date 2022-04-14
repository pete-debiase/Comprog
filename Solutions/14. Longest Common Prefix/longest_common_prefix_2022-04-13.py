#!/usr/bin/env python3
"""https://leetcode.com/problems/longest-common-prefix/"""

class Solution:
    def longestCommonPrefix(self, strings: list[str]) -> str:
        prefix = ''
        for letter_tuple in zip(*strings):
            if len(set(letter_tuple)) != 1: break
            prefix += letter_tuple[0]
        return prefix

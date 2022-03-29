#!/usr/bin/env python3
"""https://leetcode.com/problems/longest-common-prefix/"""

class Solution:
    def longestCommonPrefix(self, strings: list[str]) -> str:
        prefix = ""
        for chars in zip(*strings):
            if len(set(chars)) != 1: break
            prefix += chars[0]
        return prefix

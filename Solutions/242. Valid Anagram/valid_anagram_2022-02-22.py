#!/usr/bin/env python3
"""https://leetcode.com/problems/valid-anagram/"""

class Solution:
    def isAnagram(self, s1: str, s2: str) -> bool:
        charmap1 = self.string_to_charmap(s1)
        charmap2 = self.string_to_charmap(s2)
        return charmap1 == charmap2

    def string_to_charmap(self, string: str) -> dict[str, int]:
        charmap = {}
        for c in string:
            if c in charmap:
                charmap[c] += 1
            else:
                charmap[c] = 1
        return charmap

#!/usr/bin/env python3
"""https://leetcode.com/problems/valid-anagram/"""

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)
        return counter_s == counter_t

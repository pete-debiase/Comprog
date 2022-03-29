#!/usr/bin/env python3
"""https://leetcode.com/problems/group-anagrams/"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strings: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list)
        for string in strings:
            string_sorted = ''.join(sorted(string))
            hashmap[string_sorted].append(string)
        anagrams = list(hashmap.values())
        return anagrams

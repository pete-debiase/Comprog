#!/usr/bin/env python3
"""https://leetcode.com/problems/group-anagrams/"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strings: list[str]) -> list[list[str]]:
        anagram_dict = defaultdict(list)
        for string in strings:
            string_sorted = ''.join(sorted(string))
            anagram_dict[string_sorted].append(string)
        anagrams = list(anagram_dict.values())
        return anagrams

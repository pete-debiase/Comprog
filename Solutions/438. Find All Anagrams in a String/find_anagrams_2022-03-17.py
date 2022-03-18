#!/usr/bin/python
"""https://leetcode.com/problems/find-all-anagrams-in-a-string/"""

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        starting_indices = []
        l, r = 0, len(p)
        counter_p, counter_s = Counter(p), Counter(s[:r])

        diffs = Counter()
        for k in counter_p: diffs[k] -= counter_p[k]
        for k in counter_s: diffs[k] += counter_s[k]
        matches_needed = sum([v != 0 for v in diffs.values()])

        while r < len(s):
            if matches_needed == 0: starting_indices.append(l)
            char_l, char_r = s[l], s[r]

            diffs[char_l] -= 1
            if diffs[char_l] == 0: matches_needed -= 1
            if diffs[char_l] == -1: matches_needed += 1

            diffs[char_r] += 1
            if diffs[char_r] == 0: matches_needed -= 1
            if diffs[char_r] == 1: matches_needed += 1

            l += 1
            r += 1

        if matches_needed == 0: starting_indices.append(l)
        return starting_indices

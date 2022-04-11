#!/usr/bin/env python3
"""https://leetcode.com/problems/find-all-anagrams-in-a-string/"""

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        start_indices, l, r = [], 0, len(p)
        counter_p, counter_s = Counter(p), Counter(s[:r])

        while r < len(s):
            if counter_s == counter_p: start_indices.append(l)
            counter_s[s[r]] += 1
            counter_s[s[l]] -= 1
            l += 1
            r += 1
        if counter_s == counter_p: start_indices.append(l)
        return start_indices

    def findAnagrams2(self, s: str, p: str) -> list[int]:
        start_indices = []
        l, r = 0, len(p)
        counter_p, counter_s = Counter(p), Counter(s[:r])

        diffs = Counter()
        for k in counter_p: diffs[k] -= counter_p[k]
        for k in counter_s: diffs[k] += counter_s[k]
        matches_needed = sum(v != 0 for v in diffs.values())

        while r < len(s):
            if matches_needed == 0: start_indices.append(l)
            char_l, char_r = s[l], s[r]

            diffs[char_l] -= 1
            if diffs[char_l] == 0: matches_needed -= 1
            if diffs[char_l] == -1: matches_needed += 1

            diffs[char_r] += 1
            if diffs[char_r] == 0: matches_needed -= 1
            if diffs[char_r] == 1: matches_needed += 1

            l += 1
            r += 1

        if matches_needed == 0: start_indices.append(l)
        return start_indices

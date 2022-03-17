#!/usr/bin/python
"""https://leetcode.com/problems/permutation-in-string/"""

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)
        counter1, counter2 = Counter(s1), Counter(s2[:r])

        while r < len(s2):
            if counter1 == counter2: return True
            counter2[s2[l]] -= 1
            counter2[s2[r]] += 1
            l += 1
            r += 1
        return counter1 == counter2

class SolutionAlternate:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)
        counter1, counter2 = Counter(s1), Counter(s2[:r])

        diffs = Counter()
        for k in counter1: diffs[k] -= counter1[k]
        for k in counter2: diffs[k] += counter2[k]
        matches_needed = sum([v != 0 for v in diffs.values()])

        while r < len(s2):
            if matches_needed == 0: return True
            char_l, char_r = s2[l], s2[r]

            diffs[char_l] -= 1
            if diffs[char_l] == 0: matches_needed -= 1
            if diffs[char_l] == -1: matches_needed += 1

            diffs[char_r] += 1
            if diffs[char_r] == 0: matches_needed -= 1
            if diffs[char_r] == 1: matches_needed += 1

            l += 1
            r += 1

        return matches_needed == 0

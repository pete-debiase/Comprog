#!/usr/bin/env python3
"""https://leetcode.com/problems/permutation-in-string/"""

from collections import Counter

class SolutionRough:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, n_s1 = 0, len(s1)
        counter_s1, counter_s2 = Counter(s1), Counter(s2[l:n_s1])
        for r in range(n_s1, len(s2)):
            if counter_s2 == counter_s1: return True
            else:
                counter_s2[s2[r]] += 1
                counter_s2[s2[l]] -= 1
                l += 1
        return counter_s2 == counter_s1


class SolutionCleaner:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)
        counter1, counter2 = Counter(s1), Counter(s2[:r])

        while r < len(s2):
            if counter2 == counter1: return True
            counter2[s2[l]] -= 1
            counter2[s2[r]] += 1
            l += 1; r += 1
        return counter2 == counter1


class SolutionBest:
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

            l += 1; r += 1

        return matches_needed == 0

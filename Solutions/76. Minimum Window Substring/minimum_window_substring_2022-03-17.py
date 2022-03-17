#!/usr/bin/python
"""https://leetcode.com/problems/minimum-window-substring/"""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, substring = 0, ''
        counter = Counter(t)
        matches_needed = len(counter)

        for r in range(len(s)):
            counter[s[r]] -= 1
            if counter[s[r]] == 0:
                matches_needed -= 1

            while matches_needed == 0:
                length_window = r - l + 1
                if not substring or length_window < len(substring):
                    substring = s[l:r + 1]

                counter[s[l]] += 1
                if counter[s[l]] > 0:
                    matches_needed += 1
                l += 1

        return substring

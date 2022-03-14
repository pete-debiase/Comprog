#!/usr/bin/python
"""https://leetcode.com/problems/minimum-window-substring/"""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, substring = 0, ''
        letters = Counter(t)
        letters_needed = len(t)

        for right in range(len(s)):
            if letters[s[right]] > 0:
                letters_needed -= 1
            letters[s[right]] -= 1

            while letters_needed == 0:
                length_window = right - left + 1
                if not substring or length_window < len(substring):
                    substring = s[left:right + 1]

                letters[s[left]] += 1
                if letters[s[left]] > 0:
                    letters_needed += 1
                left += 1

        return substring

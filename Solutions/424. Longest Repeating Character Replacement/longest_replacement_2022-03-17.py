#!/usr/bin/env python3
"""https://leetcode.com/problems/longest-repeating-character-replacement/"""

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = freq_best_char = 0
        counts = defaultdict(int)
        for r in range(len(s)):
            counts[s[r]] += 1
            freq_best_char = max(freq_best_char, counts[s[r]])
            if r - l + 1 - freq_best_char > k:
                counts[s[l]] -= 1
                l += 1
        return r - l + 1

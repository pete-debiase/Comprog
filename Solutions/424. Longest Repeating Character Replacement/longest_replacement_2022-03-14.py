#!/usr/bin/python
"""https://leetcode.com/problems/longest-repeating-character-replacement/"""

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = most_uses = 0
        counts = defaultdict(int)
        for j in range(len(s)):
            counts[s[j]] += 1
            most_uses = max(most_uses, counts[s[j]])
            if j - i + 1 - most_uses > k:
                counts[s[i]] -= 1
                i += 1
        return j - i + 1

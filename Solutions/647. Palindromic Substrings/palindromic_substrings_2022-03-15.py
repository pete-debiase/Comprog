#!/usr/bin/env python3
"""https://leetcode.com/problems/palindromic-substrings/"""

class Solution:
    def countSubstrings(self, string: str) -> int:
        count = 0
        for i in range(len(string)):
            count += self._count_palindromes_around_center(string, i, i)
            count += self._count_palindromes_around_center(string, i, i + 1)
        return count

    def _count_palindromes_around_center(self, string: str, l: int, r: int) -> int:
        count = 0
        while l >= 0 and r < len(string):
            if string[l] != string[r]: break
            l -= 1
            r += 1
            count += 1
        return count

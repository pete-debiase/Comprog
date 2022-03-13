#!/usr/bin/python
"""https://leetcode.com/problems/palindromic-substrings/"""

class Solution:
    def countSubstrings(self, string: str) -> int:
        count = 0
        for i in range(len(string)):
            count += self._count_palindromes_around_center(string, i, i)
            count += self._count_palindromes_around_center(string, i, i + 1)
        return count

    def _count_palindromes_around_center(self, string: str, left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(string):
            if string[left] != string[right]: break
            left -= 1
            right += 1
            count += 1
        return count

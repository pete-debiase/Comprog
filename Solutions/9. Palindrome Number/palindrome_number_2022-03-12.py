#!/usr/bin/env python3
"""https://leetcode.com/problems/palindrome-number/"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        string_reversed = string[::-1]
        return string == string_reversed

    def is_palindrome2(self, x: int) -> bool:
        if x < 0: return False
        n, rev = x, 0
        while n:
            last_digit = n % 10
            rev = rev * 10 + last_digit
            n //= 10
        return rev == x

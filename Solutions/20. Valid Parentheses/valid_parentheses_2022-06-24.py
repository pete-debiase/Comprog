#!/usr/bin/env python3
"""https://leetcode.com/problems/valid-parentheses/"""

class Solution:
    def isValid(self, string: str) -> bool:
        brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in string:
            if c in brackets:
                stack.append(c)
            elif not stack or c != brackets[stack.pop()]:
                return False
        return not stack

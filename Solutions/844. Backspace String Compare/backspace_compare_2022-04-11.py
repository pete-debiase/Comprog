#!/usr/bin/env python3
"""https://leetcode.com/problems/backspace-string-compare/"""

import itertools

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_built = self._build(s)
        t_built = self._build(t)
        return s_built == t_built

    def _build(self, string: str) -> str:
        stack = []
        for c in string:
            if c != '#': stack.append(c)
            elif stack: stack.pop()
        return ''.join(stack)

class SolutionAlternate:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_simulate = self._simulate(s)
        t_simulate = self._simulate(t)
        are_equal = all(x == y for x, y in itertools.zip_longest(s_simulate, t_simulate))
        return are_equal

    def _simulate(self, string: str) -> str:
        skip = 0
        for c in reversed(string):
            if c == '#': skip += 1
            elif skip: skip -= 1
            else: yield c

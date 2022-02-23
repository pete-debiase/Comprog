#!/usr/bin/python
"""https://leetcode.com/problems/valid-parentheses/"""

import timeit

class SolutionInitial:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def isValid(self, string: str) -> bool:
        length = len(string)
        valid_subs = ['()', '[]', '{}']
        while length > 0:
            for sub in valid_subs:
                string = string.replace(sub, '')
            length_new = len(string)
            if length_new == length:
                return False
            else:
                length = length_new
        return True

class SolutionAlternate:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isValid(self, string: str) -> bool:
        brackets = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in string:
            if c in brackets:
                stack.append(c)
            elif not stack or c != brackets[stack.pop()]:
                return False
        return not stack


if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_alternate = SolutionAlternate()

    # Example 1 (Expected Output: True)
    s = "()"
    print(solution_initial.isValid(s))
    print(solution_alternate.isValid(s))

    # Example 2 (Expected Output: True)
    s = "()[]{}"
    print(solution_initial.isValid(s))
    print(solution_alternate.isValid(s))

    # Example 3 (Expected Output: False)
    s = "(]"
    print(solution_initial.isValid(s))
    print(solution_alternate.isValid(s))

    # Benchmarking
    s = "(]"
    print(timeit.timeit(lambda: solution_initial.isValid(s), number=100_000))
    print(timeit.timeit(lambda: solution_alternate.isValid(s), number=100_000)) # Slower

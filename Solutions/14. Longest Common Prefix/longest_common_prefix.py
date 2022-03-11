#!/usr/bin/python
"""https://leetcode.com/problems/longest-common-prefix/"""

import timeit

class SolutionInitial:
    # Time / Space Complexity: O(n) * min string length, O(1)
    def longestCommonPrefix(self, strings: list[str]) -> str:
        prefix, i = "", 0
        while True:
            try:
                chars = {_[i] for _ in strings}
                if len(chars) != 1: break
                prefix += chars.pop()
                i += 1
            except IndexError:
                break
        return prefix

class SolutionPreferred:
    # Time / Space Complexity: O(n) * min string length, O(1)
    def longestCommonPrefix(self, strings: list[str]) -> str:
        prefix = ""
        for chars in zip(*strings):
            if len(set(chars)) != 1: break
            prefix += chars[0]
        return prefix

if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_preferred = SolutionPreferred()

    # Example 1 (Expected Output: fl)
    strings = ["flower", "flow", "flight"]
    print(solution_initial.longestCommonPrefix(strings))
    print(solution_preferred.longestCommonPrefix(strings))

    # Example 2 (Expected Output: "")
    strings = ["dog", "racecar", "car"]
    print(solution_initial.longestCommonPrefix(strings))
    print(solution_preferred.longestCommonPrefix(strings))

    # Benchmarking
    number = 100_000
    strings = ["Lorem", "ipsum", "dolor", "sit", "amet,", "consectetur", "adipiscing", "elit.", "Cras", "sit", "amet", "elit", "vel", "risus", "accumsan", "luctus", "quis", "non", "orci.", "Cras."]
    print(timeit.timeit(lambda: solution_initial.longestCommonPrefix(strings), number=number))
    print(timeit.timeit(lambda: solution_preferred.longestCommonPrefix(strings), number=number))

#!/usr/bin/python
"""https://leetcode.com/problems/minimum-window-substring/"""

from collections import Counter
import timeit

class SolutionInitial:
    # Time / Space: O(s + t) / O(s + t)
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t): return ''
        left, substring = 0, ''
        counter = Counter(t)
        matches_needed = len(counter)

        for right in range(len(s)):
            counter[s[right]] -= 1
            if counter[s[right]] == 0:
                matches_needed -= 1

            while matches_needed == 0:
                len_window = right - left + 1
                if not substring or len_window < len(substring):
                    substring = s[left:right + 1]

                counter[s[left]] += 1
                if counter[s[left]] > 0:
                    matches_needed += 1
                left += 1

        return substring


if __name__ == '__main__':
    solution_initial = SolutionInitial()

    # Example 1 (Expected Output: "BANC")
    s1, s2 = "ADOBECODEBANC", "ABC"
    print(solution_initial.minWindow(s1, s2))

    # Example 2 (Expected Output: "a")
    s1, s2 = "a", "a"
    print(solution_initial.minWindow(s1, s2))

    # Example 3 (Expected Output: "")
    s1, s2 = "a", "aa"
    print(solution_initial.minWindow(s1, s2))

    # Benchmarking
    number = 10_000
    s1, s2 = "ADOBECODEBANC", "ABC"
    print(timeit.timeit(lambda: solution_initial.minWindow(s1, s2), number=number))

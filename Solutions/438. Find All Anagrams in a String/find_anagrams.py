#!/usr/bin/env python3
"""https://leetcode.com/problems/find-all-anagrams-in-a-string/"""

from collections import Counter
import timeit

class SolutionInitial:
    # Time / Space: O(n * charset), n = len(s) / O(charset)
    def findAnagrams(self, s: str, p: str) -> list[int]:
        l, r = 0, len(p)
        counter_p, counter_window = Counter(p), Counter(s[:r])
        start_indices = []

        while r < len(s):
            if counter_window == counter_p: start_indices.append(l)
            counter_window[s[l]] -= 1
            counter_window[s[r]] += 1
            l += 1
            r += 1
        if counter_window == counter_p: start_indices.append(l)
        return start_indices

class SolutionPreferred:
    # Time / Space: O(n), n = len(s) / O(charset)
    def findAnagrams(self, s: str, p: str) -> list[int]:
        l, r = 0, len(p)
        counter_p, counter_s = Counter(p), Counter(s[:r])
        start_indices = []

        diffs = Counter()
        for k in counter_p: diffs[k] -= counter_p[k]
        for k in counter_s: diffs[k] += counter_s[k]
        matches_needed = sum([v != 0 for v in diffs.values()])

        while r < len(s):
            if matches_needed == 0: start_indices.append(l)
            char_l, char_r = s[l], s[r]

            diffs[char_l] -= 1
            if diffs[char_l] == 0: matches_needed -= 1
            if diffs[char_l] == -1: matches_needed += 1

            diffs[char_r] += 1
            if diffs[char_r] == 0: matches_needed -= 1
            if diffs[char_r] == 1: matches_needed += 1

            l += 1
            r += 1

        if matches_needed == 0: start_indices.append(l)
        return start_indices


if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_preferred = SolutionPreferred()

    # Example 1 (Expected Output: [0, 6])
    s, p = "cbaebabacd", "abc"
    print(solution_initial.findAnagrams(s, p))
    print(solution_preferred.findAnagrams(s, p))

    # Example 2 (Expected Output: [0, 1, 2])
    s, p = "abab", "ab"
    print(solution_initial.findAnagrams(s, p))
    print(solution_preferred.findAnagrams(s, p))

    # Benchmarking
    number = 10_000
    s, p = "abab", "ab"
    print(timeit.timeit(lambda: solution_initial.findAnagrams(s, p), number=number))
    print(timeit.timeit(lambda: solution_preferred.findAnagrams(s, p), number=number))

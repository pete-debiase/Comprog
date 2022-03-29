#!/usr/bin/env python3
"""https://leetcode.com/problems/permutation-in-string/"""

from collections import Counter
import timeit

class SolutionInitial:
    # Doesn't pass all test cases
    # Time / Space: O(n * charset) where n = len(s2) / O(charset)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, counter1, counter2 = 0, Counter(s1), Counter()
        for r, c in enumerate(s2):
            if s2[r] not in counter1:
                counter2.clear()
                l += 1
                continue

            counter2[s2[r]] += 1
            if counter2 == counter1: return True
            if counter2[s2[r]] > counter1[s2[r]]:
                counter2[s2[l]] -= 1
                l += 1
        return False

class SolutionAlternate:
    # Good for small charsets
    # Time / Space: O(n * charset) where n = len(s2) / O(charset)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)
        counter1, counter2 = Counter(s1), Counter(s2[:r])

        while r < len(s2):
            if counter2 == counter1: return True
            counter2[s2[l]] -= 1
            counter2[s2[r]] += 1
            l += 1
            r += 1
        return counter2 == counter1

class SolutionPreferred:
    # Good for large charsets
    # Time / Space: O(n) where n = len(s2) / O(charset)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)
        counter1, counter2 = Counter(s1), Counter(s2[:r])

        diffs = Counter()
        for k in counter1: diffs[k] -= counter1[k]
        for k in counter2: diffs[k] += counter2[k]
        matches_needed = sum([v != 0 for v in diffs.values()])

        while r < len(s2):
            if matches_needed == 0: return True
            char_l, char_r = s2[l], s2[r]

            diffs[char_r] += 1
            if diffs[char_r] == 0: matches_needed -= 1
            if diffs[char_r] == 1: matches_needed += 1

            diffs[char_l] -= 1
            if diffs[char_l] == 0: matches_needed -= 1
            if diffs[char_l] == -1: matches_needed += 1

            l += 1
            r += 1

        return matches_needed == 0


if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_alternate = SolutionAlternate()
    solution_preferred = SolutionPreferred()

    # Example 1 (Expected Output: True)
    s1, s2 = "ab", "eidbaooo"
    print(solution_initial.checkInclusion(s1, s2))
    print(solution_alternate.checkInclusion(s1, s2))
    print(solution_preferred.checkInclusion(s1, s2))

    # Example 2 (Expected Output: False)
    s1, s2 = "ab", "eidboaoo"
    print(solution_initial.checkInclusion(s1, s2))
    print(solution_alternate.checkInclusion(s1, s2))
    print(solution_preferred.checkInclusion(s1, s2))

    # Benchmarking
    number = 10_000
    s1, s2 = "ab", "eidboaoo"
    print(timeit.timeit(lambda: solution_initial.checkInclusion(s1, s2), number=number))
    print(timeit.timeit(lambda: solution_alternate.checkInclusion(s1, s2), number=number))
    print(timeit.timeit(lambda: solution_preferred.checkInclusion(s1, s2), number=number))

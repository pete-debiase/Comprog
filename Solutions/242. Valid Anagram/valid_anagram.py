#!/usr/bin/env python3
"""https://leetcode.com/problems/valid-anagram/"""

import timeit
from collections import defaultdict, Counter

class SolutionInitial:
    # Time / Space: O(n) / O(n)
    def isAnagram(self, s1: str, s2: str) -> bool:
        charmap_1 = self.string_to_charmap(s1)
        charmap_2 = self.string_to_charmap(s2)
        return charmap_1 == charmap_2

    def string_to_charmap(self, a_string: str) -> dict[str, int]:
        charmap = {}
        for c in a_string:
            if c in charmap:
                charmap[c] += 1
            else:
                charmap[c] = 1
        return charmap

class SolutionPreferred:
    # Time / Space: O(n) / O(n)
    def isAnagram(self, s1: str, s2: str) -> bool:
        charmap = defaultdict(int)
        for c in s1: charmap[c] += 1
        for c in s2: charmap[c] -= 1
        return all(v == 0 for v in charmap.values())

class SolutionAlternate2:
    # Time / Space: O(n) / O(n)
    def isAnagram(self, s1: str, s2: str) -> bool:
        return Counter(s1) == Counter(s2)


if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_preferred = SolutionPreferred()
    solution_alternate2 = SolutionAlternate2()

    # Example 1 (Expected Output: True)
    s1, s2 = 'anagram', 'nagaram'
    print(solution_initial.isAnagram(s1, s2))
    print(solution_preferred.isAnagram(s1, s2))
    print(solution_alternate2.isAnagram(s1, s2))

    # Example 2 (Expected Output: False)
    s1, s2 = 'rat', 'car'
    print(solution_initial.isAnagram(s1, s2))
    print(solution_preferred.isAnagram(s1, s2))
    print(solution_alternate2.isAnagram(s1, s2))

    # Benchmarking
    s1, s2 = 'anagram', 'nagaram'
    print(timeit.timeit(lambda: solution_initial.isAnagram(s1, s2), number=100_000))
    print(timeit.timeit(lambda: solution_preferred.isAnagram(s1, s2), number=100_000)) # Slower
    print(timeit.timeit(lambda: solution_alternate2.isAnagram(s1, s2), number=100_000)) # Slower

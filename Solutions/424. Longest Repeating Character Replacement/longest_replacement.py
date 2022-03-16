#!/usr/bin/python
"""https://leetcode.com/problems/longest-repeating-character-replacement/"""

from collections import defaultdict
import timeit

class SolutionInitial:
    # Time / Space: O(n) / O(n)
    def characterReplacement(self, s: str, k: int) -> int:
        i = most_uses = 0
        counts = defaultdict(int)
        for j in range(len(s)):
            counts[s[j]] += 1
            most_uses = max(most_uses, counts[s[j]])
            if j - i + 1 - most_uses > k:
                counts[s[i]] -= 1
                i += 1
        return j - i + 1


if __name__ == '__main__':
    solution_initial = SolutionInitial()

    # Example 1 (Expected Output: 4)
    s, k = 'AABABBA', 1
    print(solution_initial.characterReplacement(s, k))

    # Example 2 (Expected Output: 4)
    s, k = 'AABABBA', 1
    print(solution_initial.characterReplacement(s, k))

    # Benchmarking
    number = 10_000
    s, k = 'AABABBA', 1
    print(timeit.timeit(lambda: solution_initial.characterReplacement(s, k), number=number))

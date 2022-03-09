#!/usr/bin/python
"""https://leetcode.com/problems/palindromic-substrings/"""

import timeit

class SolutionInitial:
    # Time / Space Complexity: O(n^3), O(1)
    def countSubstrings(self, string: str) -> int:
        n, count = len(string) + 1, 0
        for i in range(n):
            for j in range(i + 1, n):
                substring = string[i:j]
                if self._is_palindrome(substring):
                    count += 1
        return count

    def _is_palindrome(self, string: str) -> bool:
        backwards = string[::-1]
        return string == backwards

class SolutionPreferred:
    # Time / Space Complexity: O(n^2), O(1)
    def countSubstrings(self, string: str) -> int:
        pass

if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_preferred = SolutionPreferred()

    # Example 1 (Expected Output: 3)
    string = "abc"
    print(solution_initial.countSubstrings(string))
    print(solution_preferred.countSubstrings(string))

    # Example 2 (Expected Output: 6)
    string = "aaa"
    print(solution_initial.countSubstrings(string))
    print(solution_preferred.countSubstrings(string))

    # Benchmarking
    number = 10_000
    string = "aaa"
    print(timeit.timeit(lambda: solution_initial.countSubstrings(string), number=number))
    print(timeit.timeit(lambda: solution_preferred.countSubstrings(string), number=number))

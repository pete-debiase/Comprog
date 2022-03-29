#!/usr/bin/env python3
"""https://leetcode.com/problems/palindromic-substrings/"""

import timeit

class SolutionInitial:
    # Time / Space: O(n^3) / O(1)
    def countSubstrings(self, string: str) -> int:
        count, n = 0, len(string) + 1
        for i in range(n):
            for j in range(i + 1, n):
                substring = string[i:j]
                if self._is_palindrome(substring): count += 1
        return count

    def _is_palindrome(self, string: str) -> bool:
        backwards = string[::-1]
        return string == backwards

class SolutionPreferred:
    # Time / Space: O(n^2) / O(1)
    def countSubstrings(self, string: str) -> int:
        count = 0
        for i in range(len(string)):
            count += self._count_palindromes_around_center(string, i, i)
            count += self._count_palindromes_around_center(string, i, i + 1)
        return count

    def _count_palindromes_around_center(self, string: str, left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(string):
            if string[left] != string[right]: break
            left -= 1
            right += 1
            count += 1
        return count


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
    number = 1_000
    string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce finibus, ligula et hendrerit mollis, augue nibh tristique eros, sed vulputate."
    print(timeit.timeit(lambda: solution_initial.countSubstrings(string), number=number))
    print(timeit.timeit(lambda: solution_preferred.countSubstrings(string), number=number))

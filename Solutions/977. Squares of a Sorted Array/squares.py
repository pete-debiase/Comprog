#!/usr/bin/env python3
"""https://leetcode.com/problems/squares-of-a-sorted-array/"""

from collections import deque
import timeit

class SolutionInitial:
    # Time / Space: O(n log n) / O(n)
    def sortedSquares(self, nums: list[int]) -> list[int]:
        squares = [n ** 2 for n in nums]
        squares.sort()
        return squares

class SolutionAlternate:
    # Time / Space: O(n) / O(n)
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        squares = deque()
        l, r = 0, n - 1
        while l <= r:
            abs_l, abs_r = abs(nums[l]), abs(nums[r])
            if abs_l > abs_r:
                squares.appendleft(abs_l ** 2)
                l += 1
            else:
                squares.appendleft(abs_r ** 2)
                r -= 1
        return list(squares)

class SolutionPreferred:
    # Time / Space: O(n) / O(n)
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        squares = [0] * n
        l, r = 0, n - 1
        while l <= r:
            abs_l, abs_r = abs(nums[l]), abs(nums[r])
            if abs_l > abs_r:
                squares[r - l] = abs_l ** 2
                l += 1
            else:
                squares[r - l] = abs_r ** 2
                r -= 1
        return squares


if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_alternate = SolutionAlternate()
    solution_preferred = SolutionPreferred()

    # Example 1 (Expected Output: [0, 1, 9, 16, 100])
    nums = [-4, -1, 0, 3, 10]
    print(solution_initial.sortedSquares(nums))
    print(solution_alternate.sortedSquares(nums))
    print(solution_preferred.sortedSquares(nums))

    # Example 2 (Expected Output: [4, 9, 9, 49, 121])
    nums = [-7, -3, 2, 3, 11]
    print(solution_initial.sortedSquares(nums))
    print(solution_alternate.sortedSquares(nums))
    print(solution_preferred.sortedSquares(nums))

    # Benchmarking
    number = 1_000
    nums = list(range(-1000, 0)) + list(range(1000))
    print(timeit.timeit(lambda: solution_initial.sortedSquares(nums), number=number))
    print(timeit.timeit(lambda: solution_alternate.sortedSquares(nums), number=number))
    print(timeit.timeit(lambda: solution_preferred.sortedSquares(nums), number=number))

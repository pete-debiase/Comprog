#!/usr/bin/python
"""https://leetcode.com/problems/max-consecutive-ones-iii/"""

from collections import defaultdict
import timeit

class SolutionInitial:
    # Time / Space Complexity: O(n), O(1)
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = count_0s = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                count_0s += 1
            if count_0s > k:
                if nums[l] == 0: count_0s -= 1
                l += 1
        return r - l + 1

class SolutionAlternate:
    # Time / Space Complexity: O(n), O(1)
    def longestOnes(self, nums: list[int], k: int) -> int:
        l, counts = 0, defaultdict(int)
        for r in range(len(nums)):
            counts[nums[r]] += 1
            if counts[0] > k:
                counts[nums[l]] -= 1
                l += 1
        return r - l + 1

class SolutionPreferred:
    # Time / Space Complexity: O(n), O(1)
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = 0
        for r in range(len(nums)):
            k -= 1 - nums[r]
            if k < 0:
                k += 1 - nums[l]
                l += 1
        return r - l + 1


if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_alternate = SolutionAlternate()
    solution_preferred = SolutionPreferred()

    # Example 1 (Expected Output: 6)
    nums, k = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2
    print(solution_initial.longestOnes(nums, k))
    print(solution_alternate.longestOnes(nums, k))
    print(solution_preferred.longestOnes(nums, k))

    # Example 2 (Expected Output: 10)
    nums, k = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3
    print(solution_initial.longestOnes(nums, k))
    print(solution_alternate.longestOnes(nums, k))
    print(solution_preferred.longestOnes(nums, k))

    # Benchmarking
    number = 10_000
    nums, k = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3
    print(timeit.timeit(lambda: solution_initial.longestOnes(nums, k), number=number))
    print(timeit.timeit(lambda: solution_alternate.longestOnes(nums, k), number=number))
    print(timeit.timeit(lambda: solution_preferred.longestOnes(nums, k), number=number))

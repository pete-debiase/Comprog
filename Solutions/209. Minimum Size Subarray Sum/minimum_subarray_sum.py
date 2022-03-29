#!/usr/bin/env python3
"""https://leetcode.com/problems/minimum-size-subarray-sum/"""

import timeit

class SolutionInitial:
    # Time / Space: O(n) / O(n)
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left, n, length_min = 0, len(nums) + 1, float('inf')
        for right in range(n):
            while sum(nums[left:right]) >= target:
                length_min = min(length_min, right - left)
                left += 1
        return length_min if length_min != float('inf') else 0

class SolutionPreferred:
    # Time / Space: O(n) / O(1)
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        i, total, length_min = 0, 0, n + 1
        for j in range(n):
            total += nums[j]
            while total >= target:
                length_min = min(length_min, j - i + 1)
                total -= nums[i]
                i += 1
        return length_min if length_min <= n else 0


if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_preferred = SolutionPreferred()

    # Example 1 (Expected Output: 2)
    target, nums = 7, [2, 3, 1, 2, 4, 3]
    print(solution_initial.minSubArrayLen(target, nums))
    print(solution_preferred.minSubArrayLen(target, nums))

    # Example 2 (Expected Output: 1)
    target, nums = 4, [1, 4, 4]
    print(solution_initial.minSubArrayLen(target, nums))
    print(solution_preferred.minSubArrayLen(target, nums))

    # Example 3 (Expected Output: 0)
    target, nums = 11, [1, 1, 1, 1, 1, 1, 1, 1]
    print(solution_initial.minSubArrayLen(target, nums))
    print(solution_preferred.minSubArrayLen(target, nums))

    # Benchmarking
    number = 1_000
    target, nums = 200, list(range(1000))
    print(timeit.timeit(lambda: solution_initial.minSubArrayLen(target, nums), number=number))
    print(timeit.timeit(lambda: solution_preferred.minSubArrayLen(target, nums), number=number))

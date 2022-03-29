#!/usr/bin/env python3
"""https://leetcode.com/problems/two-sum/"""

import timeit

class SolutionInitial:
    # Time / Space: O(n^2) / O(1)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

class SolutionPreferred:
    # Time / Space: O(n) / O(n)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[num] = i


if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_preferred = SolutionPreferred()

    # Example 1 (Expected Output: [0,1])
    nums = [2, 7, 11, 15]
    target = 9
    print(solution_initial.twoSum(nums, target))
    print(solution_preferred.twoSum(nums, target))

    # Example 2 (Expected Output: [1,2])
    nums = [3, 2, 4]
    target = 6
    print(solution_initial.twoSum(nums, target))
    print(solution_preferred.twoSum(nums, target))

    # Example 3 (Expected Output: [0,1])
    nums = [3, 3]
    target = 6
    print(solution_initial.twoSum(nums, target))
    print(solution_preferred.twoSum(nums, target))

    # Benchmarking
    nums = list(range(100_000))
    target = 100_000
    print(timeit.timeit(lambda: solution_initial.twoSum(nums, target), number=100))
    print(timeit.timeit(lambda: solution_preferred.twoSum(nums, target), number=100))

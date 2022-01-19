#!/usr/bin/python
"""https://leetcode.com/problems/two-sum/"""

import timeit

class SolutionBrute:
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

class Solution1PassHash:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[num] = i


if __name__ == '__main__':
    solution_brute = SolutionBrute()
    solution_1passhash = Solution1PassHash()

    # Example 1 (Expected Output: [0,1])
    nums = [2, 7, 11, 15]
    target = 9
    print(solution_brute.twoSum(nums, target))
    print(solution_1passhash.twoSum(nums, target))

    # Example 2 (Expected Output: [1,2])
    nums = [3, 2, 4]
    target = 6
    print(solution_brute.twoSum(nums, target))
    print(solution_1passhash.twoSum(nums, target))

    # Example 3 (Expected Output: [0,1])
    nums = [3, 3]
    target = 6
    print(solution_brute.twoSum(nums, target))
    print(solution_1passhash.twoSum(nums, target))

    # Benchmarking
    nums = list(range(100_000))
    target = 100_000
    print(timeit.timeit(lambda: solution_brute.twoSum(nums, target), number=100))
    print(timeit.timeit(lambda: solution_1passhash.twoSum(nums, target), number=100))

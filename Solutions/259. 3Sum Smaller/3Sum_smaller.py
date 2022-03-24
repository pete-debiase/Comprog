#!/usr/bin/python
"""https://leetcode.com/problems/3sum-smaller/"""

import timeit

class Solution:
    # Time / Space: O(n^2), O(1)
    def threeSumSmaller(self, nums: list[int], target: int) -> int:
        count, n = 0, len(nums)
        nums.sort()

        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                sum_temp = nums[i] + nums[l] + nums[r]
                if sum_temp < target:
                    count += r - l
                    l += 1
                else:
                    r -= 1

        return count


if __name__ == '__main__':
    solution = Solution()

    # Example 1 (Expected Output: 2)
    nums, target = [-2, 0, 1, 3], 2
    print(solution.threeSumSmaller(nums, target))

    # Example 2 (Expected Output: 0)
    nums, target = [], 0
    print(solution.threeSumSmaller(nums, target))

    # Example 3 (Expected Output: 0)
    nums, target = [0], 0
    print(solution.threeSumSmaller(nums, target))

    # Benchmarking
    number = 10_000
    nums, target = [0], 0
    print(timeit.timeit(lambda: solution.threeSumSmaller(nums, target), number=number))

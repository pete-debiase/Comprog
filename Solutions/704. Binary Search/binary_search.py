#!/usr/bin/python
"""https://leetcode.com/problems/binary-search/"""

import timeit

class Solution:
    # Time / Space: O(log n) / O(1)
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target: l = m + 1
            elif nums[m] > target: r = m - 1
            else: return m
        return -1


if __name__ == '__main__':
    solution = Solution()

    # Example 1 (Expected Output: 4)
    nums, target = [-1, 0, 3, 5, 9, 12], 9
    print(solution.search(nums, target))

    # Example 2 (Expected Output: -1)
    nums, target = [-1, 0, 3, 5, 9, 12], 2
    print(solution.search(nums, target))

    # Benchmarking
    number = 100_000
    nums, target = [-1, 0, 3, 5, 9, 12], 2
    print(timeit.timeit(lambda: solution.search(nums, target), number=number))

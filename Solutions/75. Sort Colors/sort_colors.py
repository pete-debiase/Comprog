#!/usr/bin/env python3
"""https://leetcode.com/problems/sort-colors/"""

import timeit

class Solution:
    # Time / Space: O(n), O(1)
    def sortColors(self, nums: list[int]) -> None:
        p0, i, p2 = 0, 0, len(nums) - 1
        while i <= p2:
            if nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                p0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            else:
                i += 1


if __name__ == '__main__':
    solution = Solution()

    # Example 1 (Expected Output: [0, 0, 1, 1, 2, 2])
    nums = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums)
    print(nums)

    # Example 2 (Expected Output: [0, 1, 2])
    nums = [2, 0, 1]
    solution.sortColors(nums)
    print(nums)

    # Benchmarking
    number = 10_000
    nums = [2, 0, 1]
    print(timeit.timeit(lambda: solution.sortColors(nums), number=number))

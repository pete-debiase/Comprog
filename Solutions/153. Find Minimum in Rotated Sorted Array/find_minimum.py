#!/usr/bin/env python3
"""https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/"""

import timeit

class SolutionInitial:
    # Time / Space: O(log n) / O(1)
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        lo, hi = 0, n - 1
        if n == 1 or nums[lo] < nums[hi]: return nums[lo]

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[mid + 1]: return nums[mid + 1]
            elif nums[mid] < nums[lo]:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1


if __name__ == '__main__':
    solution_initial = SolutionInitial()

    # Example 1 (Expected Output: 1)
    nums = [3, 4, 5, 1, 2]
    print(solution_initial.findMin(nums))

    # Example 2 (Expected Output: 0)
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(solution_initial.findMin(nums))

    # Example 3 (Expected Output: 11)
    nums = [11, 13, 15, 17]
    print(solution_initial.findMin(nums))

    # Benchmarking
    number = 10_000
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(timeit.timeit(lambda: solution_initial.findMin(nums), number=number))

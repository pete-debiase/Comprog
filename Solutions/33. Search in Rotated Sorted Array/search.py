#!/usr/bin/env python3
"""https://leetcode.com/problems/search-in-rotated-sorted-array/"""

import timeit

class Solution:
    # Time / Space: O(log n) / O(1)
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    def find_rotation_index(self, nums: list[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        if n == 1: return 0
        if nums[left] < nums[right]: return 0

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return mid + 1
            elif nums[mid] < nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        return -1


if __name__ == '__main__':
    solution = Solution()

    # Example 1 (Expected Output: 4)
    nums, target = [4, 5, 6, 7, 0, 1, 2], 0
    print(solution.search(nums, target))
    # print(solution.find_rotation_index(nums))

    # Example 2 (Expected Output: -1)
    nums, target = [4, 5, 6, 7, 0, 1, 2], 3
    print(solution.search(nums, target))
    # print(solution.find_rotation_index(nums))

    # Example 2 (Expected Output: -1)
    nums, target = [1], 0
    print(solution.search(nums, target))
    # print(solution.find_rotation_index(nums))

    # Benchmarking
    number = 100_000
    nums, target = [4, 5, 6, 7, 0, 1, 2], 3
    print(timeit.timeit(lambda: solution.search(nums, target), number=number))

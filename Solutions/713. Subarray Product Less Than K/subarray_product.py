#!/usr/bin/env python3
"""https://leetcode.com/problems/subarray-product-less-than-k/"""

import timeit

class SolutionInitial:
    # Time / Space: O(n^2), O(1)
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        count, n = 0, len(nums)
        for l in range(n):
            product = nums[l]
            if product < k: count += 1
            else: continue
            for r in range(l + 1, n):
                product *= nums[r]
                if product < k: count += 1
                else: break
        return count

class SolutionPreferred:
    # Time / Space: O(n), O(1)
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1: return 0
        l, count, product = 0, 0, 1
        for r, num in enumerate(nums):
            product *= num
            while product >= k:
                product /= nums[l]
                l += 1
            count += r - l + 1
        return count


if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_preferred = SolutionPreferred()

    # Example 1 (Expected Output: 8)
    nums, k = [10, 5, 2, 6], 100
    print(solution_initial.numSubarrayProductLessThanK(nums,k))
    print(solution_preferred.numSubarrayProductLessThanK(nums,k))

    # Example 2 (Expected Output: 0)
    nums, k = [1, 2, 3], 0
    print(solution_initial.numSubarrayProductLessThanK(nums,k))
    print(solution_preferred.numSubarrayProductLessThanK(nums,k))

    # Benchmarking
    number = 100
    nums, k = [1] * 1000, 500
    print(timeit.timeit(lambda: solution_initial.numSubarrayProductLessThanK(nums,k), number=number))
    print(timeit.timeit(lambda: solution_preferred.numSubarrayProductLessThanK(nums,k), number=number))

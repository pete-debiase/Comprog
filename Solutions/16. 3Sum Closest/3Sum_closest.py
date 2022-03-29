#!/usr/bin/env python3
"""https://leetcode.com/problems/3sum-closest/"""

import timeit

class SolutionInitial:
    # Time / Space: O(n^2) / O(n)
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        dirty = diff_min = float('inf')
        n = len(nums)
        nums.sort()

        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                triplet = [nums[i], nums[l], nums[r]]
                sum_temp = sum(triplet)
                diff_temp = target - sum_temp

                if diff_temp == 0: return sum_temp
                elif diff_temp > 0: l += 1
                elif diff_temp < 0: r -= 1

                diff_min = min(diff_min, abs(diff_temp))
                if dirty != diff_min:
                    sum_closest = sum_temp
                    dirty = diff_min

        return sum_closest

class SolutionPreferred:
    # Time / Space: O(n^2) / O(n)
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n, diff_min = len(nums), float('inf')
        nums.sort()

        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                sum_temp = nums[i] + nums[l] + nums[r]
                if sum_temp < target: l += 1
                if sum_temp > target: r -= 1

                diff_temp = target - sum_temp
                if diff_temp == 0: return sum_temp
                if abs(diff_temp) < abs(diff_min):
                    diff_min = diff_temp

        return target - diff_min


if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_preferred = SolutionPreferred()

    # Example 1 (Expected Output: 2)
    nums, target = [-1, 2, 1, -4], 1
    print(solution_initial.threeSumClosest(nums, target))
    print(solution_preferred.threeSumClosest(nums, target))

    # Example 2 (Expected Output: 0)
    nums, target = [0, 0, 0], 1
    print(solution_initial.threeSumClosest(nums, target))
    print(solution_preferred.threeSumClosest(nums, target))

    # Benchmarking
    number = 10_000
    nums,  target = [0, 0, 0],  1
    print(timeit.timeit(lambda: solution_initial.threeSumClosest(nums, target), number=number))
    print(timeit.timeit(lambda: solution_preferred.threeSumClosest(nums, target), number=number))

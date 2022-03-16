#!/usr/bin/python
"""https://leetcode.com/problems/3sum/"""

import timeit

class SolutionInitial:
    # Time / Space: O(n^2) / O(n)
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0: break
            if i == 0 or nums[i] != nums[i - 1]:
                self.two_sum_ii(nums, i, triplets)
        return triplets

    def two_sum_ii(self, nums: list[int], i: int, triplets: list[list[int]]):
        i_lo, i_hi = i + 1, len(nums) - 1
        while i_lo < i_hi:
            triplet = [nums[i], nums[i_lo], nums[i_hi]]
            sum_temp = sum(triplet)
            if sum_temp < 0: i_lo += 1
            elif sum_temp > 0: i_hi -= 1
            else:
                triplets.append(triplet)
                i_lo, i_hi = i_lo + 1, i_hi - 1
                while i_lo < i_hi and nums[i_lo] == nums[i_lo - 1]:
                    i_lo += 1


if __name__ == '__main__':
    solution_initial = SolutionInitial()

    # Example 1 (Expected Output: [[-1, -1, 2], [-1, 0, 1]])
    numbers = [-1, 0, 1, 2, -1, -4]
    print(solution_initial.threeSum(numbers))

    # Example 2 (Expected Output: [])
    numbers = []
    print(solution_initial.threeSum(numbers))

    # Example 3 (Expected Output: [])
    numbers = [0]
    print(solution_initial.threeSum(numbers))

    # Example 4 (Expected Output: [[-4, 0, 4], [-4, 1, 3], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, -1, 2], [-1, 0, 1]])
    numbers = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    print(solution_initial.threeSum(numbers))

    # Benchmarking
    number = 10000
    numbers = [-1, 0, 1, 2, -1, -4]
    print(timeit.timeit(lambda: solution_initial.threeSum(numbers), number=number))

#!/usr/bin/env python3
"""https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/"""

import timeit

class SolutionInitial:
    # Time / Space: O(n) / O(1)
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i_lo, i_hi = 0, len(numbers) - 1
        while i_lo < i_hi:
            sum = numbers[i_lo] + numbers[i_hi]
            if sum == target: return [i_lo + 1, i_hi + 1]
            elif sum < target: i_lo += 1
            elif sum > target: i_hi -= 1
        return []


if __name__ == '__main__':
    solution_initial = SolutionInitial()

    # Example 1 (Expected Output: [1, 2])
    numbers, target = [2, 7, 11, 15], 9
    print(solution_initial.twoSum(numbers, target))

    # Example 2 (Expected Output: [1, 3])
    numbers, target = [2, 3, 4], 6
    print(solution_initial.twoSum(numbers, target))

    # Example 3 (Expected Output: [1, 2])
    numbers, target = [-1, 0], -1
    print(solution_initial.twoSum(numbers, target))

    # Benchmarking
    number = 100
    numbers, target = [2,7,11,15], 9
    print(timeit.timeit(lambda: solution_initial.twoSum(numbers, target), number=number))

#!/usr/bin/python
"""https://leetcode.com/problems/maximum-subarray/"""

import timeit

class SolutionInitial:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maxSubArray(self, numbers: list[int]) -> int:
        sum_current = sum_max = -float('inf')
        for number in numbers:
            sum_current = max(number, sum_current + number)
            sum_max = max(sum_current, sum_max)
        return sum_max

class SolutionPreferred():
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maxSubArray(self, numbers: list[int]) -> int:
        sum_current = sum_max = numbers[0]
        for number in numbers[1:]:
            sum_temp = sum_current + number
            sum_current = sum_temp if sum_temp > number else number
            sum_max = sum_current if sum_current > sum_max else sum_max
        return sum_max


if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_preferred = SolutionPreferred()

    # Example 1 (Expected Output: 6)
    numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution_initial.maxSubArray(numbers))
    print(solution_preferred.maxSubArray(numbers))

    # Example 2 (Expected Output: 1)
    numbers = [1]
    print(solution_initial.maxSubArray(numbers))
    print(solution_preferred.maxSubArray(numbers))

    # Example 3 (Expected Output: 23)
    numbers = [5, 4, -1, 7, 8]
    print(solution_initial.maxSubArray(numbers))
    print(solution_preferred.maxSubArray(numbers))

    # Benchmarking
    numbers = list(range(1000))
    print(timeit.timeit(lambda: solution_initial.maxSubArray(numbers), number=1000))
    print(timeit.timeit(lambda: solution_preferred.maxSubArray(numbers), number=1000))


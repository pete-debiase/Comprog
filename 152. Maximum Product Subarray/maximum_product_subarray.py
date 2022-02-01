#!/usr/bin/python
"""https://leetcode.com/problems/maximum-product-subarray/"""

import timeit

class SolutionInitial:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maxProduct(self, numbers: list[int]) -> int:
        max_current = min_current = max_final = numbers[0]
        for number in numbers[1:]:
            max_temp = max(number, max_current * number, min_current * number)
            min_current = min(number, max_current * number, min_current * number)
            max_current = max_temp
            max_final = max(max_current, max_final)
        return max_final

class SolutionAlternate:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maxProduct(self, numbers: list[int]) -> int:
        max_current, min_current, max_final = 1, 1, -float('inf')
        for n in numbers:
            x = max_current * n
            y = min_current * n
            min_current = min(n, x, y)
            max_current = max(n, x, y)
            max_final = max(max_current, max_final)
        return max_final

if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_alternate = SolutionAlternate()

    # Example 1 (Expected Output: 6)
    numbers = [2, 3, -2, 4]
    print(solution_initial.maxProduct(numbers))
    print(solution_alternate.maxProduct(numbers))

    # Example 2 (Expected Output: 0)
    numbers = [-2, 0, -1]
    print(solution_initial.maxProduct(numbers))
    print(solution_alternate.maxProduct(numbers))

    # Example 3 (Expected Output: 24)
    numbers = [-2, 3, -4]
    print(solution_initial.maxProduct(numbers))
    print(solution_alternate.maxProduct(numbers))

    # Example 4 (Expected Output: 12)
    numbers = [-4, -3, -2]
    print(solution_initial.maxProduct(numbers))
    print(solution_alternate.maxProduct(numbers))

    # Benchmarking
    numbers = list(range(1000))
    print(timeit.timeit(lambda: solution_initial.maxProduct(numbers), number=1000))
    print(timeit.timeit(lambda: solution_alternate.maxProduct(numbers), number=1000))


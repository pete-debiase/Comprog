#!/usr/bin/python
"""https://leetcode.com/problems/fruit-into-baskets/"""

import timeit
from collections import defaultdict

class SolutionInitial:
    # Time / Space Complexity: O(n), O(1)
    def totalFruit(self, fruits: list[int]) -> int:
        l, counts = 0, defaultdict(int)
        for r in range(len(fruits)):
            counts[fruits[r]] += 1
            if len(counts) > 2:
                counts[fruits[l]] -= 1
                if counts[fruits[l]] == 0: counts.pop(fruits[l])
                l += 1
        return r - l + 1


if __name__ == '__main__':
    solution_initial = SolutionInitial()

    # Example 1 (Expected Output: 3)
    fruits = [1, 2, 1]
    print(solution_initial.totalFruit(fruits))

    # Example 2 (Expected Output: 3)
    fruits = [0, 1, 2, 2]
    print(solution_initial.totalFruit(fruits))

    # Example 3 (Expected Output: 4)
    fruits = [1, 2, 3, 2, 2]
    print(solution_initial.totalFruit(fruits))

    # Benchmarking
    number = 1_000
    fruits = list(range(1000))
    print(timeit.timeit(lambda: solution_initial.totalFruit(fruits), number=number))

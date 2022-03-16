#!/usr/bin/python
"""https://leetcode.com/problems/product-of-array-except-self/"""

import math
import timeit

class SolutionInitial:
    # Time / Space: O(n^2) / O(n)
    def productExceptSelf(self, numbers: list[int]) -> list[int]:
        products = []
        for i, number in enumerate(numbers):
            temp = numbers[:]
            temp.pop(i)
            product = math.prod(temp)
            products.append(product)
        return products

class SolutionAlternate:
    # Time / Space: O(n) / O(1)
    def productExceptSelf(self, numbers: list[int]) -> list[int]:
        n = len(numbers)
        lefts, rights, products = [0]*n, [0]*n, [0]*n

        lefts[0] = 1
        for i in range(1, n):
            lefts[i] = lefts[i - 1] * numbers[i - 1]

        rights[-1] = 1
        for i in reversed(range(n - 1)):
            rights[i] = rights[i + 1] * numbers[i + 1]

        products = [left * right for left, right in zip(lefts, rights)]
        return products

class SolutionPreferred:
    # Time / Space: O(n) / O(1)
    def productExceptSelf(self, numbers: list[int]) -> list[int]:
        # Set up for ensuing traversals and calculations.
        n = len(numbers)
        products = [0] * n

        # Traverse left to right, calculating left (prefix) products.
        products[0] = 1
        for i in range(1, n):
            products[i] = products[i - 1] * numbers[i - 1]

        # Traverse right to left, calculating right (suffix) products on the fly,
        # and multiply with corresponding left products.
        right_product = 1
        for i in reversed(range(n)):
            products[i] *= right_product
            right_product *= numbers[i]

        return products


if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_alternate = SolutionAlternate()
    solution_preferred = SolutionPreferred()

    # Example 1 (Expected Output: [24, 12, 8, 6])
    numbers = [1, 2, 3, 4]
    print(solution_initial.productExceptSelf(numbers))
    print(solution_alternate.productExceptSelf(numbers))
    print(solution_preferred.productExceptSelf(numbers))

    # Example 2 (Expected Output: [0, 0, 9, 0, 0])
    numbers = [-1, 1, 0, -3, 3]
    print(solution_initial.productExceptSelf(numbers))
    print(solution_alternate.productExceptSelf(numbers))
    print(solution_preferred.productExceptSelf(numbers))

    # Benchmarking
    numbers = list(range(1_000))
    print(timeit.timeit(lambda: solution_initial.productExceptSelf(numbers), number=100))
    print(timeit.timeit(lambda: solution_alternate.productExceptSelf(numbers), number=100)) # ≈12x faster
    print(timeit.timeit(lambda: solution_preferred.productExceptSelf(numbers), number=100)) # ≈2x faster

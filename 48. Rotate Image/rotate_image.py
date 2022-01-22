#!/usr/bin/python
"""https://leetcode.com/problems/rotate-image/"""

import timeit
import numpy as np

class SolutionInitial:
    # Time Complexity: O(M) where M = number of cells in matrix
    # Space Complexity: O(1)
    def rotate(self, matrix: list[list[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

if __name__ == '__main__':
    solution_initial = SolutionInitial()

    # Example 1 (Expected Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution_initial.rotate(matrix)
    print(matrix)
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
    print()

    # Example 2 (Expected Output: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    solution_initial.rotate(matrix)
    print(matrix)
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
    print()

    # Example 3 (Expected Output: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])
    matrix = np.array([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
    rotated = np.rot90(matrix, axes=(1, 0))
    print(f'{rotated}\n')

    # # Benchmarking
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(timeit.timeit(lambda: solution_initial.rotate(matrix), number=1_000_000))
    print(timeit.timeit(lambda: np.rot90(matrix, axes=(1, 0)), number=1_000_000))

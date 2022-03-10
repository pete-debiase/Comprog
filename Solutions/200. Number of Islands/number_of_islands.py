#!/usr/bin/python
"""https://leetcode.com/problems/number-of-islands/"""

import timeit

class Solution:
    # Time / Space Complexity: O(mn), O(mn)
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid: return 0
        count, m, n = 0, len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self._dfs(grid, i, j)
                    count += 1
        return count

    def _dfs(self, grid: list[list[str]], i: int, j: int) -> None:
        m, n = len(grid), len(grid[0])
        is_oob_or_nonland = (i < 0 or i >= m or j < 0 or j >= n) or (grid[i][j] != '1')
        if is_oob_or_nonland:
            return

        grid[i][j] = '#'
        self._dfs(grid, i + 1, j)
        self._dfs(grid, i - 1, j)
        self._dfs(grid, i, j + 1)
        self._dfs(grid, i, j - 1)

if __name__ == '__main__':
    solution = Solution()

    # Example 1 (Expected Output: 1)
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    print(solution.numIslands(grid))

    # Example 2 (Expected Output: 3)
    grid = [['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']]
    print(solution.numIslands(grid))

    # Benchmarking
    number = 100_000
    grid = [['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']]
    print(timeit.timeit(lambda: solution.numIslands(grid), number=number))

#!/usr/bin/python
"""https://leetcode.com/problems/number-of-islands/"""

class Solution:
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
        if is_oob_or_nonland: return

        grid[i][j] = '#'
        self._dfs(grid, i + 1, j)
        self._dfs(grid, i - 1, j)
        self._dfs(grid, i, j + 1)
        self._dfs(grid, i, j - 1)

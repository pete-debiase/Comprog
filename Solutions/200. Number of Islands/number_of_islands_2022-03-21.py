#!/usr/bin/env python3
"""https://leetcode.com/problems/number-of-islands/"""

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        count, m, n = 0, len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self._dfs(grid, i, j)
                    count += 1
        return count

    def _dfs(self, grid: list[list[str]], i: int, j: int):
        if grid[i][j] == '#': return
        grid[i][j] = '#'

        m, n = len(grid), len(grid[0])
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for di, dj in deltas:
            i_new, j_new = i + di, j + dj
            is_in_bounds = (0 <= i_new < m) and (0 <= j_new < n)
            if is_in_bounds and grid[i_new][j_new] == '1':
                self._dfs(grid, i_new, j_new)

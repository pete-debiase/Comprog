#!/usr/bin/env python3
"""https://leetcode.com/problems/number-of-islands/"""

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]: return 0
        count, m, n = 0, len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self._dfs(grid, i, j)
                    count += 1
        return count

    def _dfs(self, grid: list[list[str]], i: int, j: int):
        m, n = len(grid), len(grid[0])
        is_oob = (i < 0 or i >= m) or (j < 0 or j >= n)
        if is_oob or grid[i][j] != '1': return

        grid[i][j] = '#'
        self._dfs(grid, i + 1, j)
        self._dfs(grid, i - 1, j)
        self._dfs(grid, i, j + 1)
        self._dfs(grid, i, j - 1)

class SolutionAlternate:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]: return 0
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
        deltas = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for di, dj in deltas:
            i_next, j_next = i + di, j + dj
            is_in_bounds = (0 <= i_next < m) and (0 <= j_next < n)
            if is_in_bounds and grid[i_next][j_next] == '1':
                self._dfs(grid, i_next, j_next)

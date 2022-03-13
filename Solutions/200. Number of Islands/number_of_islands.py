#!/usr/bin/python
"""https://leetcode.com/problems/number-of-islands/"""

import timeit
from copy import deepcopy

class SolutionInitial:
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
        deltas = ((1, 0), (-1, 0), (0, 1), (0, -1))

        grid[i][j] = '#'
        for di, dj in deltas:
            i_next, j_next = i + di, j + dj
            is_in_bounds = (0 <= i_next < m) and (0 <= j_next < n)
            if is_in_bounds and grid[i_next][j_next] == '1':
                self._dfs(grid, i_next, j_next)

class SolutionAlternate:
    # Time / Space Complexity: O(mn), O(mn)
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid: return 0
        count, m, n = 0, len(grid), len(grid[0])
        visited = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def _dfs(i: int, j: int, visited: set[tuple[int, int]]):
            if (i, j) in visited: return
            visited.add((i, j))

            for d in directions:
                i_next, j_next = i + d[0], j + d[1]
                is_in_bounds = (0 <= i_next < m) and (0 <= j_next < n)
                if is_in_bounds and grid[i_next][j_next] == '1':
                    _dfs(i_next, j_next, visited)

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == '1':
                    _dfs(i, j, visited)
                    count += 1
        return count

class SolutionAlternate2:
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

if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_alternate = SolutionAlternate()
    solution_alternate2 = SolutionAlternate2()

    # Example 1 (Expected Output: 1)
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    grid2 = deepcopy(grid)
    grid3 = deepcopy(grid)
    print(solution_initial.numIslands(grid))
    print(solution_alternate.numIslands(grid2))
    print(solution_alternate.numIslands(grid3))

    # Example 2 (Expected Output: 3)
    grid = [['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']]
    grid2 = deepcopy(grid)
    grid3 = deepcopy(grid)
    print(solution_initial.numIslands(grid))
    print(solution_alternate.numIslands(grid2))
    print(solution_alternate.numIslands(grid3))

    # Benchmarking
    number = 100_000
    grid = [['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']]
    grid2 = deepcopy(grid)
    grid3 = deepcopy(grid)
    print(timeit.timeit(lambda: solution_initial.numIslands(grid), number=number))
    print(timeit.timeit(lambda: solution_alternate.numIslands(grid2), number=number))
    print(timeit.timeit(lambda: solution_alternate.numIslands(grid3), number=number))

#!/usr/bin/python
"""https://leetcode.com/problems/merge-intervals/"""

import timeit

class SolutionInitial:
    # Time Complexity: O(n log n)
    # Space Complexity: O(n)
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        combined = []
        for interval in intervals:
            recentest = combined[-1]
            recentest_start, recentest_end = recentest[0], recentest[1]
            current_start, current_end = intervals[i][0], intervals[i][1]
            if current_start <= recentest_end:
                end = max(recentest_end, current_end)
                combined[-1] = [recentest_start, end]
            else:
                combined.append(intervals[i])
        return combined

class SolutionPreferred:
    # Time Complexity: O(n log n)
    # Space Complexity: O(n)
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_preferred = SolutionPreferred()

    # Example 1 (Expected Output: [[1, 6], [8, 10], [15, 18]])
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(solution_initial.merge(intervals))
    print(solution_preferred.merge(intervals))

    # Example 2 (Expected Output: [[1, 5]])
    intervals = [[1, 4], [4, 5]]
    print(solution_initial.merge(intervals))
    print(solution_preferred.merge(intervals))

    # Example 3 (Expected Output: [[0, 4]])
    intervals = [[1, 4], [0, 4]]
    print(solution_initial.merge(intervals))
    print(solution_preferred.merge(intervals))

    # Benchmarking
    number = 100_000
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(timeit.timeit(lambda: solution_initial.merge(intervals), number=number))
    print(timeit.timeit(lambda: solution_preferred.merge(intervals), number=number))

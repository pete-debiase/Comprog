#!/usr/bin/env python3
"""https://leetcode.com/problems/container-with-most-water/"""

import timeit

class SolutionInitial:
    # Time / Space Complexity: O(n^2) / O(1)
    def maxArea(self, heights: list[int]) -> int:
        max_area, n = 0, len(heights)
        for i in range(n):
            for j in range(i + 1, n):
                height_min = min(heights[i], heights[j])
                width = j - i
                max_area = max(max_area, height_min * width)
        return max_area

class SolutionPreferred:
    # Time / Space: O(n) / O(1)
    def maxArea(self, heights: list[int]) -> int:
        area_max, lo, hi = 0, 0, len(heights) - 1
        while lo < hi:
            width = hi - lo
            height = min(heights[lo], heights[hi])
            area_max = max(area_max, width * height)
            if heights[lo] < heights[hi]: lo += 1
            else: hi -= 1
        return area_max


if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_preferred = SolutionPreferred()

    # Example 1 (Expected Output: 49)
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(solution_initial.maxArea(heights))
    print(solution_preferred.maxArea(heights))

    # Example 1 (Expected Output: 1)
    heights = [1, 1]
    print(solution_initial.maxArea(heights))
    print(solution_preferred.maxArea(heights))

    # Benchmarking
    number = 10_000
    heights = [1,8,6,2,5,4,8,3,7]
    print(timeit.timeit(lambda: solution_initial.maxArea(heights), number=number))
    print(timeit.timeit(lambda: solution_preferred.maxArea(heights), number=number))

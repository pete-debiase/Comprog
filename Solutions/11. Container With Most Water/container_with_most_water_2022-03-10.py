#!/usr/bin/python
"""https://leetcode.com/problems/container-with-most-water/"""

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        area_max, left, right = 0, 0, len(heights) - 1
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            area_max = max(area_max, height * width)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return area_max

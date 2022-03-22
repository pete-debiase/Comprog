#!/usr/bin/python
"""https://leetcode.com/problems/squares-of-a-sorted-array/"""

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        l, r = 0, n - 1
        squares = [0] * n
        while l <= r:
            abs_l, abs_r = abs(nums[l]), abs(nums[r])
            if abs_l > abs_r:
                squares[r - l] = nums[l] ** 2
                l += 1
            else:
                squares[r - l] = nums[r] ** 2
                r -= 1
        return squares

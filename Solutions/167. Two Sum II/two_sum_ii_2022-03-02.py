#!/usr/bin/env python3
"""https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i_lo, i_hi = 0, len(numbers) - 1
        while i_lo < i_hi:
            sum_temp = numbers[i_lo] + numbers[i_hi]
            if sum_temp == target: return [i_lo + 1, i_hi + 1]
            elif sum_temp < target: i_lo += 1
            elif sum_temp > target: i_hi -= 1
        return []

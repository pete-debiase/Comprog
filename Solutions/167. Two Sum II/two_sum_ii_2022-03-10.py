#!/usr/bin/python
"""https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            sum_temp = numbers[left] + numbers[right]
            if sum_temp == target:
                return [left + 1, right + 1]
            elif sum_temp < target:
                left += 1
            else:
                right -= 1
        return []

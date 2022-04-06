#!/usr/bin/env python3
"""https://leetcode.com/problems/3sum-smaller/"""

class Solution:
    def threeSumSmaller(self, nums: list[int], target: int) -> int:
        count, n = 0, len(nums)
        nums.sort()

        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < target:
                    count += r - l
                    l += 1
                else:
                    r -= 1

        return count

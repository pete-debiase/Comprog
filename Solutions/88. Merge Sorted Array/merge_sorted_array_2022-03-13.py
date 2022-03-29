#!/usr/bin/env python3
"""https://leetcode.com/problems/merge-sorted-array/"""

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1, p2, p_write = m - 1, n - 1, m + n - 1
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p_write] = nums1[p1]
                p1 -= 1
            else:
                nums1[p_write] = nums2[p2]
                p2 -= 1
            p_write -= 1

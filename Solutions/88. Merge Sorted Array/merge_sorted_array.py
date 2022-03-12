#!/usr/bin/python
"""https://leetcode.com/problems/merge-sorted-array/"""

import timeit

class SolutionInitial:
    # Time / Space Complexity: O(n+m log m+n), O(n)
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[m: m + n] = nums2
        nums1.sort()

class SolutionPreferred:
    # Time / Space Complexity: O(n + m), O(1)
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


if __name__ == '__main__':
    solution_initial = SolutionInitial()
    solution_preferred = SolutionPreferred()

    # Example 1 (Expected Output: [1,2,2,3,5,6])
    nums1, m, nums2, n = [1,2,3,0,0,0], 3, [2,5,6], 3
    solution_initial.merge(nums1, m, nums2, n)
    print(nums1)
    solution_preferred.merge(nums1, m, nums2, n)
    print(nums1)

    # Example 2 (Expected Output: [1])
    nums1, m, nums2, n = [1], 1, [], 0
    solution_initial.merge(nums1, m, nums2, n)
    print(nums1)
    solution_preferred.merge(nums1, m, nums2, n)
    print(nums1)

    # Example 2 (Expected Output: [1])
    nums1, m, nums2, n = [0], 0, [1], 1
    solution_initial.merge(nums1, m, nums2, n)
    print(nums1)
    solution_preferred.merge(nums1, m, nums2, n)
    print(nums1)

    # Benchmarking
    number = 1
    nums1, m, nums2, n = (list(range(100_000)) + [0] * 100_000), 100_000, list(range(100_000)), 100_000
    print(timeit.timeit(lambda: solution_initial.merge(nums1, m, nums2, n), number=number))
    print(timeit.timeit(lambda: solution_preferred.merge(nums1, m, nums2, n), number=number))

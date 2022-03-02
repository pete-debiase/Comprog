#!/usr/bin/python
"""https://leetcode.com/problems/reverse-linked-list/"""

import timeit

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SolutionIterative:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev

class SolutionRecursive:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node

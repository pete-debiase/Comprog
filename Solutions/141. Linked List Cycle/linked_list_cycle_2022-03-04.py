#!/usr/bin/env python3
"""https://leetcode.com/problems/linked-list-cycle/"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False

    def hasCycle2(self, head: ListNode | None) -> bool:
        seen, node = set(), head
        while node:
            if node in seen: return True
            seen.add(node)
            node = node.next
        return False

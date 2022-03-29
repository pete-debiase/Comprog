#!/usr/bin/env python3
"""https://leetcode.com/problems/linked-list-cycle/"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False

class SolutionAlternate:
    def hasCycle(self, head: ListNode | None) -> bool:
        node, nodes = head, set()
        while node:
            if node in nodes: return True
            nodes.add(node)
            node = node.next
        return False

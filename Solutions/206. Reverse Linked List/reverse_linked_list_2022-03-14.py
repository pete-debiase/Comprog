#!/usr/bin/python
"""https://leetcode.com/problems/reverse-linked-list/"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev, node = None, head
        while node:
            temp = node
            node = node.next
            temp.next = prev
            prev = temp
        return prev

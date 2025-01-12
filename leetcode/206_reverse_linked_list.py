"""206. Reverse Linked List"""
from typing import Optional

class ListNode:
    """Definition for singly-linked list node"""
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

# pylint: disable=too-few-public-methods
class Solution:
    """Solution class for reversing a linked list"""

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a linked list iteratively.
        
        Args:
            head: Head of the linked list to reverse
            
        Returns:
            ListNode: Head of the reversed linked list
        """
        if not head:
            return None

        cur = head
        prev = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev
    

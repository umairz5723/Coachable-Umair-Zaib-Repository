"""160. Intersection of Two Lists"""
from typing import Optional

# pylint: disable=too-few-public-methods
class ListNode:
    """Definition for singly-linked list node"""
    def __init__(self, val=0, next_node=None):  # Changed 'next' to 'next_node'
        self.val = val
        self.next = next_node

class Solution:
    """Solution class for finding intersection of two linked lists"""

    def get_intersection_node(self, head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
        """
        Find the intersection node of two linked lists using the two pointer technique.
        
        Args:
            head_a: Head of first linked list
            head_b: Head of second linked list
            
        Returns:
            ListNode: Intersection node if exists, else None
        """
        p1 = head_a
        p2 = head_b

        while p1 != p2:
            p1 = p1.next if p1 else head_a
            p2 = p2.next if p2 else head_b

        return p1
    

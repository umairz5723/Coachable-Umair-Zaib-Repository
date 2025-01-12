"""23. Merge K Sorted Lists"""

from typing import List
import heapq

class Solution:
    """Solution Class"""
  
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        This function makes use of a heap to first heappush every element in ever list within lists.
        We then construct a node "cur" which will be used to construct the remaindar of the list.
        Lastly we pop from our pq using heappop to create the next Node, a new ListNode and iterate to it.
        """
        if not list:
            return
        
        pq = []

        for lst in lists:

            cur = lst
            while cur:
                heapq.heappush(pq, cur.val)
                cur = cur.next
        
        cur = ListNode(0, None)
        head = cur

        while pq:
            cur.next = ListNode(heapq.heappop(pq), None)
            cur = cur.next
        
        return head.next

"""215. Kth Largest in a Array """

import heapq
from typing import List

class Solution:
    """ Solution class """
    def find_kth_largest(self, nums: List[int], k: int) -> int:

        """
        Function to find the k largest
        element in "nums" using a 
        heap.
        """
        pq = []

        for num in nums:

            if len(pq) < k:
                heapq.heappush(pq, num)
            else:
                if pq[0] < num:
                    heapq.heappop(pq)
                    heapq.heappush(pq, num)

        return pq[0]

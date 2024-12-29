"""215. Kth Largest in a Array """
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        pq = []

        for num in nums:

            if len(pq) < k:
                heapq.heappush(pq, num)
            else:
                if pq[0] < num:
                    heapq.heappop(pq)
                    heapq.heappush(pq, num)
        
        return pq[0]

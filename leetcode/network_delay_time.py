""" 743. Network Delay Time """


from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    """ Solution Class """
    def netork_delay_time(self, times, n, k) -> int:

        """
        This function calculates the minimum time
        it takes for all nodes to recieve the
        a signal.

        - Convert this problem into a graph 
            and traverse it in an optimal way

        - Implement Dijstraks Algorithm: 
            Always choose the smaller weight path

        - Keep track of these optimal times using a dictionary

        - If the length of these min_times == n 
        (number of nodes):
            - return the MAXIMUM value of min_times
            which is the final node to recieve the singal (minimum time)

        Time Complexity: O((V+E) Log V) 
            - Heap Operations for each Vertex
        Space Complexity: O(V + E) 
            on our min heap, adj_list dict, and min_times dict
        """

        adj_list = defaultdict(list)

        for source, target, time in times:
            adj_list[source].append((target, time))

        min_times = defaultdict(int)
        pq = [(0,k)]

        while pq:
            cur_time, idx = heappop(pq)

            if idx in min_times:
                continue

            min_times[idx] = cur_time

            for neighbor, neighbor_time in adj_list[idx]:
                if neighbor not in min_times:
                    heappush(pq, (cur_time + neighbor_time, neighbor))

        if len(min_times) == n:
            return max(min_times.values())

        return -1

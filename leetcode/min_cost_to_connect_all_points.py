""" 1584. Min Cost to Connect All Points """

import heapq
from typing import List

class Solution:
    """ Solution Class """
    def min_cost_connect_points(self, points: List[List[int]]) -> int:
        """
        This function uses Prims Algorithm
        to construct a MST using all of the
        available points.

        We use a Min Heap so that we can always
        extract the smallest manhattan distance
        avaliable and add it to our MST. 

        The process:
            Extract the smallest distance along with its
            index from the min heap, skipping indexes that
            have already been used. 

            Add this minimum distance to the total distance
            and iterate over all of the points again, skipping
            indexes we have already used:
                - Calculate the manhattan distance of the unused
                point and push it into our min heap.
        
        Time Complexity: O(N^2 * Log N) - Due to nested loop that 
        runs len(points) time, using the heappush method which is O(log N) 
        Space Complexity: O(P) - Number of points in our stack 
        """

        total_points = len(points)
        connected_points = 0
        total_cost = 0
        visited = set()
        pq = [(0,0)]

        while connected_points < total_points:
            # Extract the minimum distance
            dist, idx = heapq.heappop(pq)

            if idx in visited:
                continue

            visited.add(idx)
            total_cost += dist
            connected_points += 1

            # Extract xi,yi
            x1, y1 = points[idx]

            # Loop through the other points to
            # extract manhattan distance
            for i in range(total_points):
                if i not in visited:
                    x2, y2 = points[i]
                    man_dist = abs(x1 - x2) + abs(y1 - y2)
                    # Push the distance, index into the heap
                    heapq.heappush(pq, (man_dist, i))

        return total_cost

""" 210. Course Schedule II """

from typing import List
from collections import defaultdict

class Solution:

    """ Solution Class """

    def find_order(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:

        """

        This function makes use of an adj_list
        to simulate nodes (prequisites) and edges (courses).
        Using this and a visited list (0: not visited, 1: visiting, 2: visiting),
        we can perform DFS/Topsort to verify that there aren't any cycles 
        (unable to finish all courses). After we mark
        each course as visited (removing it as a depedency), 
        we also append it to a result list. Lastly,
        which we must return the list in reverse order
        to ensure the correct ordering.
        
        """
        adj_list = defaultdict(list)

        for crs,pre in prerequisites:
            adj_list[pre].append(crs)

        visited = [[0] for _ in range(num_courses)]
        res = []

        def dfs(crs):
            # If the course is still being visited, there is a cycle (no valid ordering possible)
            if visited[crs] == 1:
                return False
            # The course has already visited/completed we can continue DFS
            if visited[crs] == 2:
                return True

            visited[crs] = 1
            for course in adj_list[crs]:
                if not dfs(course):
                    return False

            visited[crs] = 2
            res.append(crs)
            return True

        for i in range(num_courses):
            if not dfs(i):
                return []

        return res[::-1]
        

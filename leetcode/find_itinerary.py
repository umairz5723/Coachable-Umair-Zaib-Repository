""" 332. Reconstruct Itinerary """

from typing import List
from collections import defaultdict

class Solution:
    """ Solution Class """
    def find_itinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        This function uses Iterative DFS
        to reconstruct an itinerary in 
        lexical order.

        This means should we have a departing
        airport that maps to more than one
        arrival airport, we always pick the
        smaller lexical order.

        1) Construct an adjacency list from
        the tickets sorted in descending order.
        This way we can always select the smaller
        lexical order by popping from the back of the
        values list.

        2) Implement a stack to simulate DFS where:
            A - We add popped elements to the stack 
            for further exploration, where the action 
            of popping simulates us visiting the arrival
            airport.
            
            B - Or add the top element in our stack to a 
            result, meaning it has been fully processed.
            (No more airports to go)

        We return the result list in reverse to maintain 
        the correct order, this is because we only add to the
        result AFTER we are done processing all all of its paths.

        Time Complexity: O(N Log N) 
        Space Complexity: O(N)

        """

        # Construct the adj_list
        adj_list = defaultdict(list)

        for source, target in sorted(tickets, reverse = True):
            adj_list[source].append(target)


        # Perform Iterative DFS
        stack = ["JFK"]
        res = []

        while stack:

            # Go to the lexographically smaller string (airport):
            if adj_list[stack[-1]]:
                stack.append(adj_list[stack[-1]].pop())
            else:
                # The current airport has no more destinations
                # We have fully processed it
                res.append(stack.pop())

        return res[::-1]

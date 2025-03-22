""" 787. Cheapest Flights Within K Stops """

from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    """ Solution Class """
    def find_cheapest_price(self, flights, src, dst, k):
        """
        This function calculates the 
        cheapest flights within K
        stops.

        - Build an adj_list of flights
        where the key is the source, and the value(s)
        are the (target,price).
        - Keep track of the best prices seen thus far
        in the best_prices dict.
        - Use a priority queue to simulate each stop:
            - Where we gather the current price of the
            trip and stops remaining thus far.
            - We search for all options at a given city, updating
            the price if needed. The city with the least cost 
            will always be explored next in the priority queue.
        - If our pq empties out, this means we were unable to make 
        it to the target destination within K stops.

        Time Complexity: O(N log N)
        Space Complexity: O(N)
        """
        # Create an adj_list
        adj_list = defaultdict(list)
        for source, target, price in flights:
            adj_list[source].append((target, price))

        # Store the best prices
        best_prices = {}
        # Initialize a min heap
        #   Price, city, stops
        pq = [(0, src, k + 1)]

        while pq:
            price, city, stops = heappop(pq)

            # We've found the dest city within K stops
            if city == dst:
                return price

            if stops > 0:
                # Continue exploration by calculating the cumlative price
                # to go to the next city
                for neighbor, neighbor_price in adj_list[city]:
                    new_price = price + neighbor_price

                    # Create an entry or update an existy one for the neighbor city,
                    # adjusting the price and stops for the next heappop
                if ((neighbor, stops - 1) not in best_prices or
                best_prices[(neighbor, stops - 1)] > new_price):
                    best_prices[(neighbor, stops - 1)] = new_price
                    heappush(pq, (new_price, neighbor, stops - 1))

        # Unable to reach dst within K stops
        return -1

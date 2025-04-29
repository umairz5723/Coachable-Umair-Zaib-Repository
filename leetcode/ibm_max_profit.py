""" IBM Max Profit """
from typing import List

class Solution:

    """ Solution Class """

    def max_profit(self, cost: List[int], x: int) -> int:
        """
         This function calculates the maximum
         profit possible within the budget "x".

         Each item has a cost and associated profit
         of '2^i', where 'i' is the index of the item.
         Our goal is to maximize the total profit while
         ensuring the total_cost of selected items 
         is within the budget "x".

         We first create a list of items which pairs
         the original cost array with the index it
         resides in. We then sort this based on the
         desc order of the INDEX because they will 
         potentially yield the highest profit (larger
         value for 'i').

         Our final step is to loop over the items 
         list and calculate a total_cost and 
         total_profit such that is less than the
         input value "x". 

        """

        mod = 10**9 + 7
        n = len(cost)

        # Pair each cost with its index (for profit calculation)
        items = [(cost[i], i) for i in range(n)]


        # Sort items in descending order of index (higher profit first)
        items.sort(key=lambda item: -item[1])

        total_profit = 0
        total_cost = 0

        # Going through the sorted items list
        # Verify that adding the cost at the current i
        # Won't give us an integer larger than x (within budget)
        for current_cost, idx in items:
            if total_cost + current_cost <= x:
                total_cost += current_cost
                total_profit = (total_profit + pow(2, idx, mod)) % mod

        return total_profit

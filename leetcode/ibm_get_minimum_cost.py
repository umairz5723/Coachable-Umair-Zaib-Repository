""" ibm_get_minimum_cost """

class Solution:

    """ Solution Class"""

    def get_min_cst(self, edge_cost: int, input_cost: int, bundle_cost: int, x: int, y: int) -> int:
        """
        This method handles three scenarios of buying:
        1) Buying both edge and input parts seperately

        2) Buying the lowest amount of bundles to secure
        the amount of parts needed for the smaller amount
        between edge_cost/input_cost.

        3) Buying the largest amount of bundles possible
        to fulfill the amount for both edge_cost and 
        input_cost. 

        """
        # By each part seperately 
        seperate_cost = (edge_cost * x) + (input_cost * y)

        # By enough bundles to fulfill the requirement for X or Y
        # Then buy the remaining parts seperately, one of the calculation will cancel out
        # where (y-y) = 0 or (x-x) = 0 * anything = 0.
        min_bun = bundle_cost * min(x,y) + (x - min(x,y)) * edge_cost + (y - min(x,y)) * input_cost

        # By meeting the requirement for the maximum between x,y we also meet the requirement for min
        max_bun = bundle_cost * max(x,y) 

        return min(seperate_cost, min_bun, max_bun)


""" Minimum Difference """

from typing import List

class Solution:
    """ Solution Class """
    def ibm_minimum_difference2(self, measurements: List[int]) -> List[List[int]]:
        """
        This function solves the minimum difference problem
        by sorting the input list to extract the existing
        minimum difference.
        
        We then iterate over the sorted list again to collect
        all pairs that have a difference that matches our
        min_diff variable.
        """
        # Sort the list to extract the min diff
        measurements.sort()
        min_diff = float("inf")

        for i in range(len(measurements)-1):
            min_diff = min(min_diff, abs(measurements[i+1]-measurements[i]))

        res = []
        # Now loop through the sorted list again and collect all pairs that have the min_diff
        for i in range(len(measurements)-1):
            if abs(measurements[i+1] - measurements[i]) == min_diff:
                res.append([measurements[i], measurements[i+1]])

        return res

""" IBM Maximum Efficiency """

from typing import List

class Solution:
    """ Solution Class """
    def maximum_efficiency(self, n: int, arrival_time: List[int]) -> float:
        """
        This function calculates the maximum 
        efficiency between two intervals [t1,t2]
        where the active time is denoted as:
            t2 - t1
        and the efficency is denoted as:
            efficiency = 2 / active_time

        The process:
        1) Sort the arrival_time list, this will
        give us the most optimal intervals because
        they are closest in values when sorted.
        2) Initalize a max_efficiency to detect 
        and replace the maximum efficiency we may
        come across.
        3) Iterate over the arrival_time list:
         - Determine the pair t1,t2
         - Calculate the active_time (t2 - t1)
         - Calculate the efficiency (2 - active_time)
         - Replace the maximum_efficiency as needed.
         
        """
        # Step 1: Sort the arrival times
        arrival_time.sort()

        # Step 2: Initialize maximum efficiency
        max_efficiency = float('-inf')

        # Step 3: Iterate through consecutive pairs
        for i in range(1, n):
            t1 = arrival_time[i - 1]
            t2 = arrival_time[i]

            # Active time
            active_time = t2 - t1

            # Efficiency for this interval
            efficiency = 2 - active_time

            # Update maximum efficiency
            max_efficiency = max(max_efficiency, efficiency)

        # Step 4: Return the maximum efficiency
        return max_efficiency

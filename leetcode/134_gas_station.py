from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Determines the starting gas station index where the car can complete a circuit.
        """

        # Check if a complete circuit is possible
        if sum(gas) < sum(cost):
            return -1

        remaining_gas = 0
        start_index = 0

        # Traverse through each station
        for i in range(len(gas)):
            remaining_gas += gas[i] - cost[i]

            # If remaining gas is negative, reset start index and remaining gas
            if remaining_gas < 0:
                remaining_gas = 0
                start_index = i + 1

        return start_index

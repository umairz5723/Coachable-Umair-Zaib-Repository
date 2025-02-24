""" 853. Car Fleet """

from typing import List

class Solution:

    """ Solution Class """

    def car_fleet(self, target: int, position: List[int], speed: List[int]) -> int:

        """
        This function uses a stack approach to 
        generate the number of car fleets that will
        arrive at the destination target.

        - We process the cars closest to the target using the
        starting position merged with the speed (sorted).
        - We then calculate the time it will take each car 
        to reach the target.
        - We append the time of a given car when it has a larger 
        value of "time", which means it will not be able to catch up
        the the car at the top of the stack (ahead of it), thus forming 
        a new car fleet.

        Time Complexity: O(N Log N) - Sorting
        Space Complexity: O(N) - Stack Space
        """

        # Merge the cars starting position with its speed and sort it
        # So we can process the cars that are closest to the
        # to the target first
        cars = sorted(zip(position, speed), reverse = True)
        stack = []

        # Calculate the time it will take each car to reach the target
        for pos, spd in cars:

            time = (target - pos) / spd

            # A new fleet forms if the current car takes longer than the car ahead of it
            # (i.e., it cannot catch up). We append this time to the stack.
            if not stack or stack[-1] < time:
                stack.append(time)

        # The length of the stack represents the number of fleets
        return len(stack)

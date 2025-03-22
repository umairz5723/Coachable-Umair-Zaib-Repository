""" 875. Koko Eating Bananas"""

import math

class Solution:
    """ Solution Class """
    def min_eating_speed(self, piles, h):
        """
        This function calculates
        the minimum speed at which
        Koko can eat and complete each
        pile of bananas in piles.

        - Use binary search to search a 
        RANGE of times from (1, maximum
        pile within piles)
        - Calculate the speed "k" of which
        Koko will eat at.
        - Determine how long it will take to
        finish ALL piles.
        - Try for a smaller speed if the 
        total_hours to complete the piles 
        is less than "h".
        - Speed up if we aren't able to
        complete all piles within "h" hours.

        Time Complexity: O(N) - Searching for maximum
        value in piles
        Space Complexity: O(1)

        """
        lo = 1
        hi = max(piles)

        while lo < hi:
            # Mid represents the speed at which we eat
            mid = (lo + hi) // 2

            # Calculate the time it will take
            # To finish everything at this speed "mid"
            total_hours = sum(math.ceil(pile / mid) for pile in piles)

            if total_hours <= h:
                # Try eating at a slower speed
                hi = mid
            else:
                # We can't finish everything at the current
                # Speed of "mid"
                # Increment lo to speed up the pace of eating
                lo = mid + 1

        return lo

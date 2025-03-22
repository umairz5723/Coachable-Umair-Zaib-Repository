""" 42. Trapping Rain Water """

from typing import List

class Solution:
    """ Solution Class """
    def trap(self, height: List[int]) -> int:
        """
        This function uses a two-pointer
        to compute how much water we can 
        trap after raining. 

        We make use of a maximum seen 
        thus far from both sides (pointers).
        Using this, we update our result
        using the equal/smaller of the two.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """

        if len(height) <= 2:
            return 0

        lmax = height[0]
        rmax = height[-1]

        l = 1
        r = len(height) - 2

        res = 0

        while l <= r:
 
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])


            if lmax <= rmax:
                res += lmax - height[l]
                l += 1
            else:
                res += rmax - height[r]
                r -= 1

        return res
    

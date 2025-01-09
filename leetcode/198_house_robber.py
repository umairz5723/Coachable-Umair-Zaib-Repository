""" 198. House Robber """

from typing import List

class Solution:
    """ Solution Class"""

    def rob(self, nums: List[int]) -> int:
        
        """
        This function makes use of two variables "prev" which will essentially represent two houses ago,
        and "cur" will represent the running maximum/one house ago. We extract a max_val at each step in our loop
        to compare whether we want to keep our current maximum (one house ago) or rob two houses ago + the current house.
        The "cur" variable will always reflect the maximum value thus it is the one to get returned.
        """

        if len(nums) <= 2:
            return max(nums)
        
        prev = 0
        cur = 0

        for house in nums:
            max_val = max(cur, prev + house)
            prev = cur
            cur = max_val

        return cur

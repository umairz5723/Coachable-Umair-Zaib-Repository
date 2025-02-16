""" 78. Subsets """

from typing import List

class Solution:
    """ Solution Class """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        This function makes use of DFS/Backtracking
        to explore every possible combinational 
        subset of "nums".

        Out DFS method explores a given index and returns
        when we hit the basecase of "idx" >= len(nums). At this
        step we make a copy of the currenet subset list and add
        it to the result list to avoid any ovewriting.

        The recursive calls are broken into two:
            1) Include the current integer at "idx" and make a recursive
            call to "idx + 1"
            2) Exlcude (pop from subset list) and make a recursive call
            to "idx + 1"

        Time Complexity: O(2^N)
        Space Complexity: O(N)
        """
        res = []
        subset = []

        def dfs(idx):
            if idx >= len(nums):
                res.append(subset.copy())
                return

            # Include number at idx
            subset.append(nums[idx])
            dfs(idx + 1)

            # Exclude the number at idx
            subset.pop()
            dfs(idx + 1)

        dfs(0)
        return res

""" 46. Permutations """

from typing import List

class Solution:

    """ Solution Class """

    def permute(self, nums: List[int]) -> List[List[int]]:

        """
        This solution uses backtracking
        to collect all the possible permutations
        that exist given a list "nums".

        We use the backtrack method:
            Basecase: 
                When the length of the 
                current permutation we have just 
                built is == nums, we can then collect
                it as a valid answer.

            Recursive step:
                - Iterate through each number
                - Verify that the number isn't already
                in the current permutation.
                - Add the valid number into the permutation
                - Call backtrack to collect another number
                / hit the basecase.
                - Pop the number(s) after we have successfully
                add a permutation to the result list.

        Time Complexity: O(N!)
        Space Complexity: O(N)

        """
        res = []
        perm = []

        def backtrack():
            """
            Recursive function to build
            permutation.
            """
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for num in nums:
                if num not in perm:
                    perm.append(num)
                    backtrack()
                    perm.pop()

        backtrack()
        return res

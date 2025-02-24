""" 39. Combination Sum """

from typing import List

class Solution:

    """ Solution Class """

    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        This function makes use of 
        a backtracking method to 
        dynamically build a path of 
        integers that equal that input
        "target". 
        
        Time Complexity: O(2^T) where T is the ratio of the target 
        to the smallest candidate. This is because each recursive 
        call either includes or excludes a candidate, 
        leading to exponential growth.

        Space Complexity: O(K * M) where K is the number of
        valid combinations and M is the maximum length of 
        the valid combinations.

        """

        res = []
        path = []

        def backtrack(idx):
            """
            Recursive method for building
            a list of integers that may add up
            to the target.

            Basecase: We have a path of integers that
            == target, append it to the result.

            Boundary checks:
            - Verify that idx is inbounds and that the 
            current path sum isnt > target.

            Recursive calls:
                - Exclude the current idx element and try 
                the next index
                - Include the current element to be potentially
                used multiple times.

            Backtrack by removing current index element and trying
            another combination.

            """
            if sum(path) == target:
                res.append(path.copy())
                return

            # Cover the cases where idx or path sum is too large
            if idx >= len(candidates) or sum(path) > target:
                return

            # Exclude the current candidate and move to the next one
            backtrack(idx + 1)

            # Include the current candidate and retry to allow multiple inclusions
            path.append(candidates[idx])
            backtrack(idx)

            # Backtrack by removing the last element to explore other combinations
            path.pop()

        backtrack(0)
        return res

""" 55. Jump Game"""

from typing import List

class Solution:
    """ Solution Class """
    def can_jump(self, nums: List[int]) -> bool:
        """
        Function to determine if we can
        "jump" to the last index of the 
        "nums" list. 
        """
        moves = 0

        for num in nums:
            if moves < 0:
                return False
            if num > moves:
                moves = max(moves, num)
            moves -= 1

        return True

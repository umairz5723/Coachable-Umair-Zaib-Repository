from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        moves = 0

        for num in nums:
            if moves < 0:
                return False
            elif num > moves:
                moves = num
            moves -= 1

        return True

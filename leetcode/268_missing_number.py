"""268. Missing Number"""

from typing import List

class Solution:
   """Solution Class"""
  
    def missingNumber(self, nums: List[int]) -> int:
       """
       This function finds the missing number in the nums array by
       using XOR to effectively cancel out all the existing numbers,
       leaving use with the number that is missing within the range
       of numbers within the input list
       """
        res = len(nums)
        for i in range(len(nums)):
            res ^= nums[i] ^ i
        
        return res

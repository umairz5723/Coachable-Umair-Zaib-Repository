"""136. Single Number"""
from typing import List

class Solution:
  """Solution Class""""
  
    def singleNumber(self, nums: List[int]) -> int:
        """
        This method makes use of the XOR function to to obtain the unique element that appears only one time in the list.
        Because the XOR of a number againist itself will essentially cancel out and be equal to zero, we will be left with
        (0 xor unique_element) = unique_element.
        """
        res = 0
        for num in nums:
            res = num ^ res
        
        return res

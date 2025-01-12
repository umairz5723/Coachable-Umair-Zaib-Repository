"""338. Counting Bits"""
from typing import List

class Solution:
  """Solution Class"""
  
    def countBits(self, n: int) -> List[int]:
        """
        The solution makes use of of the Right Shift Operation which shifts the binary representation of a number one position to the right.
        The other necessary operation is the Bitwise AND Operation which essentially determines whether the input number is odd or even,
        where we add 0 if even or 1 if odd. At each iteration in the loop, we look at the "parent binary number" which we have previous calculated 
        and add either a 0 or 1 to it based on if "i" is even or odd. 
        """
        ans_array = [0] * (n+1)

        for i in range(n+1):
            ans_array[i] = ans_array[i>>1] + (i&1) 
        
        return ans_array

""" 238. Product of Array Except Self """ 
from typing import List

class Solution:
    """ Solution Class """
    def product_except_self(self, nums: List[int]) -> List[int]:
        """
        This function implements the usage/combination
        of prefix and postfix products to get the product
        of all elements except nums[i].

        1) Initialize an answer list, prefix, and postfix
           all with 1.

        2) Calculate the prefix product and store it in answer[i]:
            - Store the prefix product at the current index.
            - Update the prefix by multiplying it with nums[i].
              This gives the product of all elements before nums[i].

        3) Finalize answer[i] by calculating the postfix product:
            - Traverse the array in reverse order.
            - Multiply answer[i] by the current postfix product.
            - Update the postfix using nums[i] * postfix.
        
        By combining the prefix and postfix, we get the product 
        of all elements before and after a given index. 

        Time Complexity: O(N)
        Space Complexity: O(1) (ignoring the output array)
        """

        answer = [1] * len(nums)
        nums_length = len(nums)
        prefix = 1
        postfix = 1

        # Calculate the prefix product
        for i in range(nums_length):
            answer[i] = prefix
            prefix *= nums[i]

        # Calculate the postfix product
        for j in range(nums_length -1, -1 ,-1):
            answer[j] *= postfix
            postfix *= nums[j]


        return answer

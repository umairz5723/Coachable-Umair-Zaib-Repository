""" 66. Plus One """

from typing import List

class Solution:

    """ Solution Class """

    def plus_one(self, digits: List[int]) -> List[int]:
        """
        This function uses a pointer to iterate
        over digits in a backwards fashion. We either
        return digits (after adding 1) when we find find an index that
        doesn't have a value of 9 or must go through the entire digits
        list to keep track of a carry-over value.

        As we loop:
            Case 1: We are at an element that isn't 9
                - Add one to the value and return digits
            
            Case 2: Current value is a 9
                - Set the element = 0
                - Decrement the idx pointer

        If the loop terminates, this means every value in digits
        was a 9, we must create an index with the
        value of 1 to the front of digits and return it.

        Time Complexity: O(N)
        Space Complexity: O(N) if we count the input list digits as space
        """
        # Start from the final index and iterate backwards
        idx = len(digits) - 1

        while idx >= 0:

            if digits[idx] < 9:
                digits[idx] += 1
                return digits

            digits[idx] = 0
            idx -= 1

        # We've fallen off the list which means
        # Each value in digits was 9 and is now 0
        # Add an integer element 1 to the front of the list
        return [1] + digits

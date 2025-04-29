""" Maximize Resource Allocations"""

from typing import List
from collections import defaultdict

class Solution:
    """ Solution Class """
    def maximize_resource_allocation(self, arr: List[int], k: int) -> int:
        """
        This function uses the sliding window 
        technique get the sum of windows that
        contain unique elements of size k.

        1) We initialze the first window manually
        2) Go through the remainder of the array:
            - Remove the leftmost element
            - Add the rightmost element
            - Collect a new potential max_sum
            if the frequency dictionary contains
            exactly k entries.

        """
        if len(arr) < k:
            return -1

        # Initialize frequency counter and current sum
        freq = defaultdict(int)
        curr_sum = 0
        max_sum = float('-inf')

        # Initialize the first window
        for i in range(k):
            freq[arr[i]] += 1
            curr_sum += arr[i]

        # Check first window
        if len(freq) == k:
            max_sum = curr_sum

        # Slide the window
        for i in range(k, len(arr)):
            # Remove the leftmost element
            freq[arr[i-k]] -= 1
            if freq[arr[i-k]] == 0:
                del freq[arr[i-k]]
            curr_sum -= arr[i-k]

            # Add the new element
            freq[arr[i]] += 1
            curr_sum += arr[i]

            # Update max_sum if current window has all unique elements
            if len(freq) == k:
                max_sum = max(max_sum, curr_sum)

        if max_sum == float('inf'):
            return -1

        return max_sum

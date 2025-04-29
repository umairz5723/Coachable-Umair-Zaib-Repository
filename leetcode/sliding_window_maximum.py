""" 239. Sliding Window Maximum """

from typing import List
from collections import deque

class Solution:

    """ Solution Class"""

    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:

        """
        This function uses a monotonically decreasing
        queue to extract the maximum value in a window
        of size "k". In doing so, we do not have to store
        the actual size of the window at all times.

        As we iterate over nums:
        1) Remove the rightmost elements in the deque
        if the incoming number is larger to maintain
        a monotonically decreasing. This means the largest
        value will always be at q[0]

        2) Verify the leftmost element (index) q[0] is still
        within the current window. The only possible candidate 
        for this is the element at (idx - k).

        3) Start appending the maximum value after we 
        cross idx crosses k-1 (the size of the window).

        Time complexity: O(N)
        Space complexity: O(K) - Size of deque

        """
        q = deque()
        max_values = []

        for idx, cur_num in enumerate(nums):

            # Remove rightmost element(s) if incoming number is larger
            while q and nums[q[-1]] < cur_num:
                q.pop()
            q.append(idx)

            # Remove element that has become stale if it exists
            if q[0] == idx - k:
                q.popleft()

            # Collect the max values when we have a suitable window size
            if idx >= k - 1:
                max_values.append(nums[q[0]])

        return max_values

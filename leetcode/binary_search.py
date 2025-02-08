""" 704. Binary Search """
from typing import List

class Solution:
    """ Solution Class """

    def search(self, nums: List[int], target: int) -> int:
        """
        Implements binary search to find the target index.
        Returns -1 if the target is not found.
        """
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1

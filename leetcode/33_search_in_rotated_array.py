"""33. Search In Rotated Array"""
from typing import List


class Solution:
    """Class implementing search in a rotated sorted array."""

    def search(self, nums: List[int], target: int) -> int:
        """
        Search for target in a rotated sorted array.

        Args:
            nums: A list of integers that was rotated an unknown number of times
            target: The integer to search for

        Returns:
            int: The index of target if found, -1 otherwise
        """
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid

            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1

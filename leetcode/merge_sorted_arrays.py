""" 88. Merge Sorted Arrays """

from typing import List

class Solution:

    """ Solution Class """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        This function utilizies pointers for nums1, nums2, "p".
        We work backwards for each array, moving towards the front, 
        because everything is in sorted order we can maintain this order by 
        selecting the larger number at each step. We take an element from either array,
        and decrement the pointer of that array, also decrementing "p" for the next valid position. 
        Lastly, we verify that any remaining elements in nums2 are placed into nums1.
        Time complexity: O(N + M)
        Space complexity: O(1)
        """

        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:

            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

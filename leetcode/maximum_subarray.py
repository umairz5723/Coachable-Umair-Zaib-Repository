""" 53. Maximum Subarray """

from typing import List

class Solution:
    """ Solution Class """

    def max_sub_array(self, nums: List[int]) -> int:
        """
        Function ti extract the maximum
        subarray using the sliding window
        technique.
        """

        cul_sum = 0
        maximum = float("-inf")


        for num in nums:
            cul_sum += num
            maximum = max(maximum, cul_sum)
            cul_sum = max(cul_sum, 0)

        return maximum

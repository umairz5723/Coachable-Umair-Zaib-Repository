from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cul_sum = 0
        maximum = -inf

        for i in range(len(nums)):
            cul_sum += nums[i]
            maximum = max(maximum, cul_sum)

            if cul_sum < 0:
                cul_sum = 0

        return maximum

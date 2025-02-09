""" 91. Decode Ways"""

from typing import List

class Solution:
    """ Solution Class """
    def numDecodings(self, s: str) -> int:
        """
        This function utilizies a DP array to store calculations from previous steps.
        We loop through the string and verify whether we have a single digit and/or double_digit,
        where we add to the current index from i-1 if we have a valid single digit and do the same 
        for i-2 when we have a valid double digit.

        """
        if s[0] == "0":
            return 0
        
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(s)+1):
            single_digit = int(s[i-1])
            double_digit = int(s[i-2:i])

            if single_digit != 0:
                dp[i] += dp[i-1]
            if  10 <= double_digit <= 26:
                dp[i] += dp[i-2] 

        return dp[-1]

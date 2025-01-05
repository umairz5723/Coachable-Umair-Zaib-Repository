""" 5. Longest Palindromic Substring """

from typing import List

class Solution:
        """ Solution Class """
    def longestPalindrome(self, s: str) -> str:
        """
        
        This function makes use of a helper method "expand" to expand left and right pointers
        and return palindrome.
        We collect palindromes of odd and even length on the main loop and replace the existing
        longest plaindrome seen thus far if needed.

        """
        if len(s) == 1:
            return s[0]
        
        def expand(l,r):

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]

        res = [s[0]]

        for i in range(len(s)-1):
            odd = expand(i,i)
            even = expand(i, i+1)

            if len(odd) > len(res[0]):
                res[0] = odd
            if len(even) > len(res[0]):
                res[0] = even
        
        return res[0]

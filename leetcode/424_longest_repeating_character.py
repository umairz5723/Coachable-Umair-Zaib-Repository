""" 424. Longest Repeating Character Replacement """

from collections import defaultdict

class Solution:
    """ Solution Class """
    def characterreplacement(self, s: str, k: int) -> int:

        """
        This function uses the sliding window technique
        where valid windows are determined by the difference
        between the window length and the maximum freq
        of a given character in the "freq" dict. This works 
        because we are making anywhere from 0 to k replacements.
        If the difference is greater than K we know we must 
        shrink the window as won't have enough replacements 
        possible.

        Time Complexity: O(N)
        Space Complexity: O(1) - Only storing 26 characters
        """

        freq = defaultdict(int)
        left = 0
        max_length = 0

        for right in range(len(s)):

            freq[s[right]] += 1
            window = right - left + 1

            if window - max(freq.values()) <= k:
                max_length = max(max_length, window)
            else:
                freq[s[left]] -= 1
                left += 1

        return max_length

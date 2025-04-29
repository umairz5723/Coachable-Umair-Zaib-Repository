""" final_string """

class Solution:

    """ Solution Class"""

    def get_final_string(self, s: str) -> str:
        """
        This function uses a stack to
        create and determine the final string.

        Anytime we run into the letter "S"
        we check if "A" and "W" exist at the 
        top of the stack. If so, we pop from 
        the stack twice and don't place the "S".
        This will remove all occurences of "AWS".
        """

        stack = []
        for ch in s:
            if ch == "S" and len(stack) >= 2 and stack[-1] == "W" and stack[-2] == "A":
                stack.pop()
                stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack) if stack else -1

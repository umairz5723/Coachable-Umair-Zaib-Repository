""" 2. Add Two Numbers """


class ListNode:
    """ ListNode Class """
    def __init__(self, val=0):
        """
        Function to initalize a ListNode.
        """
        self.val = val
        self.next = None

class Solution:
    """ Solution Class """
    def add_two_numbers(self, l1, l2):

        """
        This function adds two Linked
        Lists together.

        We initalize a carry_over variable
        in the event that our calculation 
        ends up in a sum greater than 9.
        While both pointers are valid,
        We initalize the values at each
        pointer:
            - Calculate the sum
            - Extract the single digit result
            - Carry over a digit if needed

        We build the newly summed linked list
        at each step using a dummy node to 
        begin with.

        Time Complexity: O(N)
        Space Complexity: O(N)
        
        """
        dummy = ListNode()
        cur = dummy
        carry_over = 0

        while l1 or l2 or carry_over:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            l_sum = l1_val + l2_val + carry_over
            digit = l_sum % 10
            carry_over = l_sum // 10

            cur.next = ListNode(digit)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next


        return dummy.next

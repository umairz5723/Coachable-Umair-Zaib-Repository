"""98. Validate Binary Search Tree"""

class Solution:
  """Solution Class"""
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        The solution makes use a recursive method "validate" and a minimum/maximum value.
        We ensure that the node being processes is neither <= to an existing minimum
        and not >= an existing maximum. 
        We make recursive calls to node.left by passing in whatever the minimum may be, and the current node's value as the maximum.
        We make recurisve calls to node.right by passing in the current node's value as the minimum and whatevere the maximium is at the time of the call.
        """
      
        min_val = None
        max_val = None

        def validate(node, minimum, maximum):
            if not node:
                return True
            
            if (minimum is not None and node.val <= minimum) or (maximum is not None and node.val >= maximum):
                return False
            
            left = validate(node.left, minimum, node.val)
            right = validate(node.right, node.val, maximum)

            return left and right
        
        return validate(root, min_val, max_val)

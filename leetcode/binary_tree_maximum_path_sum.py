""" 124. Binary Tree Maximum Path Sum """

class TreeNode():
    """ Tree Node Class"""
    def __init__(self, x):
        """ 
        Function to initialize TreeNode class
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """ Solution Class """
    def max_path_sum(self, root:TreeNode) -> int:
        """
        This function calculates the maximum
        sum path possible within a given Binary
        Tree.

        - Initalize the root value as the max_sum

        DFS Method:
            Basecase:
                return 0 when we dont have a node

            Recursive steps:
                Go down left subtree
                Go down right subtree
            
            Option one to calculate max_sum:
                - Use the current parent node and both
                child nodes as a path (valid)
            
            Option two that will get passed upward in the
            recursion stack to parent node:
                - Return the sum of the current node plus 
                the LARGER child node. 
                - We ignore negative values by returning 
                the maximum of (0, the result of the step above)

        Time Complexity: O(N)
        Space Complexity: O(H) - height of tree
        """

        max_sum = root.val

        def dfs(node):
            if not node:
                return 0

            left_path = dfs(node.left)
            right_path = dfs(node.right)

            # Going down a path in both directions
            nonlocal max_sum
            max_sum = max(max_sum, node.val + left_path + right_path)

            return max(0, node.val + max(left_path, right_path))


        dfs(root)
        return max_sum

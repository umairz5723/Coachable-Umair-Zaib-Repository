""" 572. Subtree of Another Tree """

from typing import Optional

class TreeNode:
    """ Definition for a binary tree node. """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """ Solution Class """

    def is_sub_tree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        """ Determines if subRoot is a subtree of root. """

        def compare(node1, node2):
            """ Compares two trees for identical structure and values. """
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return compare(node1.left, node2.left) and compare(node1.right, node2.right)

        q = [root]

        while q:
            curr = q.pop(0)

            if curr.val == sub_root.val:
                if compare(curr, sub_root):
                    return True

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        return False

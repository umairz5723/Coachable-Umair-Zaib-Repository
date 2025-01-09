"""572. Subtree of Another Tree"""

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        def compare(node1,node2):
            if not node1 and not node2:
                return True
            if node1 and not node2 or node2 and not node1:
                return False
            if node1.val != node2.val:
                return False
            return compare(node1.left, node2.left) and compare(node1.right, node2.right)
        
        q = [root]

        while q:
            curr = q.pop(0)

            if curr.val == subRoot.val:
                if compare(curr,subRoot) == True: return True
            
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)

        return False

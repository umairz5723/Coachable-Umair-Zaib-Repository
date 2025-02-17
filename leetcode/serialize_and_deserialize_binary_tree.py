""" 297. Serialize and Deserialize Binary Tree """ 

class TreeNode(object):
    """ Tree Node Class"""
    def __init__(self, x):
        """ 
        Function to initialize TreeNode class
        """
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """ Solution Class """
    def serialize(self, root):
        """
        This function uses preorder 
        traversal to construct of a string
        that represents the binary tree 
        "root" being passed in. 

        Preorder method:
            Basecase: No Node, append "None"
            - Append the current valid Node value
            to the string list
            - Recursive calls to the left and right node
        
        Preorder is a great option here because it will
        preserve the tree's structure, where we can easily 
        map leaf node, allowing us to know when subtrees end.

        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        string = []

        def preorder(node):
            if not node:
                string.append("None")
                return

            string.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ','.join(string)

    def deserialize(self, data):
        """
        This function takes a string data
        as input. We split the string on the 
        comma delimiter and loop through the 
        indicies using DFS.

        DFS method:
            - Skips indexes that are "None"
            - Creates the root node
            - Increments the index to the next element
            - Recursively builds the left subtree
            - Recursively builds the right subtree
        Time Complexity: O(N)
        Space Complexity: O(N)
        """

        if not data:
            return []

        data = data.split(",")
        i = 0
        def dfs():
            nonlocal i
            if data[i] == "None":
                i += 1
                return None

            node = TreeNode(int(data[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()

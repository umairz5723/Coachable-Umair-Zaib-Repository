""" 79. Word Search """

from typing import List

class Solution:

    """ Solution Class """

    def exist(self, board: List[List[str]], word: str) -> bool:

        """
        This function uses DFS and backtracking to
        return whether we are able to search for the 
        input "word" using the given constraints.

        DFS Method:
            Basecase: If the index passed in
            is == length of the input word we have
            successfully searched the existence of 
            the word.

            - Handle boundary checks, visited set to avoid
            re-using the same cell, and character mismatch

            - Peform DFS on the 4 neighbors, if any of these calls
            hit the basecase return True.
            - Should all the search paths fail, backtrack by removing 
            the current (r,c) from the visited set to be reused.

        Time Complexity: O(M*N * 4^L) where L represents the path of a search
        Space Complexity: O(W), where W is the length of the word

        """

        rows = len(board)
        cols = len(board[0])
        visited = set()

        # DFS method to explore a given cell
        def dfs(r,c,idx):

            """
            This function performs DFS search to
            search down a given row,col and index 
            for a potential match for a character 
            in "word". 
            """

            # Basecase to conclude VALID search
            if idx == len(word):
                return True

            # Boundary checks, visited and character mismatch
            if r<0 or r>=rows or c < 0 or c >= cols or (r,c) in visited or board[r][c] != word[idx]:
                return False

            # Check these neighbor cells for the next character (paths)
            # If any of these paths result in the hitting the basecase
            # we can return true
            visited.add((r,c))
            if(
                dfs(r+1,c,idx+1) or
                dfs(r-1,c,idx+1) or
                dfs(r,c+1,idx+1) or
                dfs(r,c-1,idx+1)
            ): return True

            # Backtrack
            visited.remove((r,c))
            return False


        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True

        return False

""" 289. Game of Life """

from typing import List

class Solution:
    """ Solution Class  """
    def game_of_life(self, board: List[List[int]]) -> None:
        """
        The solution uses two loops to solve this problem, one
        to setup state-change and the other to confirm it.
        
        The helper method get_live_neighbors returns all
        living cell neighbors, by verifing that they are 
        inbounds and have a cell value of > 0.

        The initial loop alters to the board such that:
            1's: replaced with 2's if neighbors != 2 or 3
            0's: replaced with -1's if neighbors = 3
        
        The purpose of replacing with 2 is done such that
        we can still use it a live neighbor to another cell.
        
        The purpose of replacing with -1's is done such that
        it wont be included as a live cell and we know it will
        be flipped in the final loop.

        Time Complexity: O(M*N)
        Space Complexity: O(1)
        """

        rows = len(board)
        cols = len(board[0])

        def get_live_neighbors(i,j):
            live_neighbors = -board[i][j]

            for r in range(i-1, i+2):
                for c in range(j-1, j+2):
                    if 0 <= r < rows and 0 <= c < cols and board[r][c] > 0:
                        live_neighbors += 1

            return live_neighbors


        # Inital Loop
        for r in range(rows):
            for c in range(cols):

                live_neigh = get_live_neighbors(r,c)

                if board[r][c] == 1 and live_neigh < 2 or board[r][c] == 1 and live_neigh > 3:
                    board[r][c] = 2
                if board[r][c] == 0 and live_neigh == 3:
                    board[r][c] = -1

        # Final State Loop
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 0
                if board[r][c] == -1:
                    board[r][c] = 1

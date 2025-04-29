""" 529. Minesweeper """

from typing import List

class Solution:
    """ Solution Class """
    def update_board(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """
        This function implements DFS to
        search the board and make the necessary
        changes. 
        For every coordinate in the stack:
            We check if it is E:
                - Count the mines in the neighbor cells
                - When mines == 0, mark the current cell as 'B'
                and append all neighbors to the stack
                - Othewise append the number of mines in the
                  8 neighbor cells.
        Time complexity: O(M*N)
        Space complexity: O(M*N) - DFS stack space
        """

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        rows = len(board)
        cols = len(board[0])
        neighbors = [(-1,0), (-1,1), (-1,-1), (0,1), (0,-1), (1,0), (1,1), (1,-1)]
        stack = [(click[0],click[1])]

        while stack:
            r,c = stack.pop()

            if board[r][c] == 'E':
                mines = 0

                for row, col in neighbors:
                    dr = r + row
                    dc = c + col

                    if 0 <= dr < rows and 0 <= dc < cols and board[dr][dc] == 'M':
                        mines += 1

                if mines == 0:
                    board[r][c] = 'B'

                    for row, col in neighbors:
                        dr = r + row
                        dc = c + col

                        if 0 <= dr < rows and 0 <= dc < cols:
                            stack.append((dr,dc))
                else:
                    board[r][c] = str(mines)

        return board

""" 51. N-Queens """

from typing import List

class Solution:

    """ Solution Class """

    def solve_n_queens(self, n: int) -> List[List[str]]:
        """
        This function uses backtracking to solve
        the N-Queens problem. 

        Constraints: 
        We can't have more than one Q in the
        same row, column, positive diagonal (r+c),
        or negative diagonal (r-c). 

        The diagonals are helpful because each
        cell will have a constant positive or 
        negative diagonal, no matter the row.
        We use sets for each of these positions
        to avoid placement.

        The backtracking process:
            -If we find a valid cell, we place a 
            "Q" and add all the necessary info into
            the corresponding sets. 
            -We then call recursively call the next
            row backtrack(r+1). 
            -If our call ends up being a dead-end
            we remove the "Q" we recently placed
            and try another column.

        Time complexity: O(N!)
        Space complexity: O(N^2) for the board
        """
        cols = set()
        pos_diag = set()
        neg_diag = set()

        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)

            for c in range(n):
                if c in cols or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue

                board[r][c] = "Q"
                cols.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)

                backtrack(r+1)

                cols.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return res

""" 37. Sudoku Solver """

from typing import List
from collections import defaultdict, deque

class Solution:
    """ Solution Class """
    def solve_sudoku(self, board: List[List[str]]) -> None:

        """
        This function uses DFS for number
        placement and backtracking.

        Setup:
        - Create dictionaries to keep track
        of the numbers in each row, column, 
        and 3x3 sub-boxes (boxes).
        - Initialize a queue that will:
            - Collect every existing number
            and add it into the 3 dictionaries
            - Add the row and column of each 
            empty cell into the queue for number
            placement

        DFS Method:
            - Basecase: Empty q = Search concluded
            - Otherwise:
                Extract the current row, column and sub-box.
                Loop for each number[1,9]:
                    - For any number that ISN'T in all 3 sets:
                        - Add it to the board + dictionaries
                        - Recursively call DFS to verify if the
                        current number placed is viable
                        - Backtrack if needed, appending the 
                        row and column back into the front of the
                        deque.

        Time complexity: O(9^N)
        Space complexity: O(N)

        """

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        q  = deque()

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    boxes[(r//3,c//3)].add(board[r][c])
                else:
                    q.append((r,c))


        def dfs(q):
            if not q:
                return True

            r,c = q.popleft()
            b = (r//3, c//3)

            for num in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                if num not in rows[r] and num not in cols[c] and num not in boxes[b]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[b].add(num)

                    if dfs(q):
                        return True

                    board[r][c] = "."
                    rows[r].discard(num)
                    cols[c].discard(num)
                    boxes[b].discard(num)

            q.appendleft((r,c))
            return False

        dfs(q)

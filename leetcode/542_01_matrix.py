""" 542. 01 Matrix """

from typing import List
from collections import deque

class Solution:
    """Class containing matrix distance calculation methods."""

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Updates matrix with distances to nearest zero.

        Args:
            mat (List[List[int]]): Input matrix containing 0s and 1s

        Returns:
            List[List[int]]: Matrix with each cell containing distance to nearest 0
        """
        if not mat:
            return mat

        rows = len(mat)
        cols = len(mat[0])
        queue = deque()

        # Initialize matrix and queue
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = float('inf')

        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # BFS to update distances
        while queue:
            row, col = queue.popleft()

            for row_offset, col_offset in neighbors:
                new_row = row + row_offset
                new_col = col + col_offset

                if (0 <= new_row < rows and 
                    0 <= new_col < cols and 
                    mat[new_row][new_col] > mat[row][col]):
                    
                    queue.append((new_row, new_col))
                    mat[new_row][new_col] = mat[row][col] + 1

        return mat

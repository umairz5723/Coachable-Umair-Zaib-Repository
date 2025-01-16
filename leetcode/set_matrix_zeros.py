""" 73. Set Matrix Zeroes """

from typing import List
class Solution:

    """ Solution Class """

    def set_zeroes(self, matrix: List[List[int]]) -> None:
        """
        This function makes use of of the
        first row/column as indicators and two boolean flag
        variables to ensure a O(1) Space Complexity. 
        
        We first check whether there exists a 0 in the
        first row and column (True/False). If there is, we
        know that once we set the inner matrix 0's we must also
        manually set the first row/column to 0 afterwards. 

        We then loop over the matrix, if at any point we come across a 0,
        we set the first cell in the first row/col to a 0 as well, indicating
        that the entire row/col will become 0.

        The second loop then fills the matrix with 0's, excluding the 0th row/col.
        Once this is done as a last step because we must first use 
        these cells to know which rows/cols to set 0's to.

        Algorithm:
        1. Store whether first row/col originally contain any zeros
        2. Use first row/col as markers: for any cell matrix[i][j] = 0,
        set matrix[i][0] and matrix[0][j] = 0 to mark that row/col
        3. Fill inner matrix (excluding first row/col) based on markers
        4. Finally, set first row/col to zero if they originally contained zeros
        
        """

        rows = len(matrix)
        cols = len(matrix[0])

        zero_in_first_row = 0 in matrix[0]
        zero_in_first_col = any(row[0] == 0 for row in matrix)

        for r in range(1,rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if zero_in_first_row:
            matrix[0] = [0] * cols

        if zero_in_first_col:
            for row in matrix:
                row[0] = 0
        

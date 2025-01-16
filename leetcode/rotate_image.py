""" 48. Rotate Image """

from typing import List
class Solution:

    """ Solution Class """

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        This function makes use of the conceopt of 
        transposing a matrix, we first iterate over the matrix
        to swap values along the main diagnal, (0,0), (1,1), ...
        This works because transposing the matrix will put each
        integer in the correct row. Once it is in the correct 
        row, we can reverse each row to place each number in the 
        correct column.

        Time Complexity: O(N^2)
        Space: O(1)
        """

        # First transpose the matrix
        rows = len(matrix)
        for i in range(rows):
            for j in range(i+1, rows):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for row in matrix:
            l = 0
            r = rows - 1

            while l < r:
                row[l], row[r] = row[r], row[l]
                r -= 1
                l += 1

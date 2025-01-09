""" 62. Unique Paths """

from typing import List

class Solution:
    
    """ Solution Class """

    def uniquePaths(self, m: int, n: int) -> int:
        """
        
        This function solves the unique paths problem by solving via bottom-up approach.
        We set the base cases of the last row and col to be all 1's
        We then calculate the unique path of a given cell by the sum of the right neighbor and bottom neighbor.
        This will eventually lead us back to the top-left corner which will contain the number of unqiue paths from the top-left
        to bottom-right corner.

        """
        rows = m
        cols = n

        grid = [[0 for j in range(cols)] for i in range(rows)]
        
        for i in range(rows):
            grid[i][cols-1] = 1
        for j in range(cols):
            grid[rows-1][j] = 1
        
        for i in range(rows-2, -1, -1):
            for j in range(cols-2, -1,-1):
                grid[i][j] = grid[i+1][j] + grid[i][j+1]
        
        return grid[0][0]
        

""" 1020. Number of Enclaves"""

from typing import List

class Solution:
    """ Solution Class """

    def num_enclaves(self, grid: List[List[int]]) -> int:
        """

        This function uses DFS to verify paths from 
        the boundary cells of the grid. Upon each
        sucessfull search, we set the cell's value
        to zero, meaning it has been visited and
        that it be used to walk off the boundary of 
        the grid. Cells have values of 1 but are
        unable to be reached from our DFS search
        will appropirately remain 1 as they
        cannot reach the boundary cells. Lastly
        we return the sum of each row to collect
        all the remaining 1's in the grid after DFS.

        Time complexity: O(M*N)
        Space complexity: O(M*N) - recursion stack

        """
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return

            grid[r][c] = 0
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        # Loop through first and last row
        for j in range(cols):
            if grid[0][j] == 1:
                dfs(0,j)
            if grid[rows-1][j] == 1:
                dfs(rows-1,j)

        # Loop through first and last col
        for i in range(rows):
            if grid[i][0] == 1:
                dfs(i,0)
            if grid[i][cols-1] == 1:
                dfs(i,cols-1)

        return sum(sum(row) for row in grid)

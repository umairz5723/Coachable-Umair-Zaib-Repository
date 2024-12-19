"""
Module for simulating orange rotting process in a grid.
This solution calculates the minimum time until all fresh oranges become rotten.
"""

from typing import List
from collections import deque

class Solution:
    """Class containing methods for orange rotting simulation."""

    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Calculates minimum time for all fresh oranges to become rotten.

        Args:
            grid (List[List[int]]): Grid where:
                0 represents empty cell
                1 represents fresh orange
                2 represents rotten orange

        Returns:
            int: Minimum minutes until all oranges rot, -1 if impossible, 0 if no fresh oranges
        """
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        rotten = 0
        queue = deque()

        # Count fresh and rotten oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten += 1
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        # Handle base cases
        if fresh == 0:
            return 0
        if not queue and fresh > 0:
            return -1

        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = -1

        # BFS to rot oranges
        while queue:
            current_level = len(queue)

            for _ in range(current_level):
                row, col = queue.popleft()

                for row_offset, col_offset in neighbors:
                    new_row = row + row_offset
                    new_col = col + col_offset

                    if (0 <= new_row < rows and 
                        0 <= new_col < cols and 
                        grid[new_row][new_col] == 1):
                        
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = 2
                        fresh -= 1
            minutes += 1

        return -1 if fresh > 0 else minutes

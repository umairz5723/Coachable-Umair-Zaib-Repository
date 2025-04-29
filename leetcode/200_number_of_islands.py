from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])
        visited: set = set()
        islands: int = 0

        def bfs(queue: List[tuple[int, int]]) -> None:
            """Perform BFS to explore the entire island."""
            while queue:
                row, col = queue.pop(0)
                neighbors = [(-1, 0), (1, 0), (0, 1), (0, -1)]

                for r, c in neighbors:
                    dr = row + r
                    dc = col + c

                    if (
                        0 <= dr < rows
                        and 0 <= dc < cols
                        and (dr, dc) not in visited
                        and grid[dr][dc] == "1"
                    ):
                        visited.add((dr, dc))
                        queue.append((dr, dc))

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == "1":
                    visited.add((i, j))
                    bfs([(i, j)])
                    islands += 1

        return islands

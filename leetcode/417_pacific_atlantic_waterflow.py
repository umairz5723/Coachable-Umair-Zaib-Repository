from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Find cells that can flow to both Pacific and Atlantic oceans.
        
        Args:
            heights (List[List[int]]): 2D grid of terrain heights
        
        Returns:
            List[List[int]]: List of [row, col] coordinates that can flow to both oceans
        """
        if not heights or not heights[0]:
            return []

        rows = len(heights)
        cols = len(heights[0])
        atl_q = []
        pac_q = []
        atl_set = set()
        pac_set = set()

        # Initialize Pacific ocean edges
        for i in range(rows):
            pac_q.append((i, 0))
            pac_set.add((i, 0))

        # Initialize Atlantic ocean edges
        for j in range(cols):
            pac_q.append((0, j))
            pac_set.add((0, j))

        # Initialize Pacific ocean edges
        for i in range(rows):
            atl_q.append((i, cols - 1))
            atl_set.add((i, cols - 1))

        # Initialize Atlantic ocean edges
        for j in range(cols):
            atl_q.append((rows - 1, j))
            atl_set.add((rows - 1, j))

        # Possible movement directions
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(queue: List[tuple], visited: set) -> None:
            """
            Perform breadth-first search to find reachable cells.
            
            Args:
                queue (List[tuple]): Initial queue of coordinates
                visited (set): Set to track visited coordinates
            """
            while queue:
                row, col = queue.pop(0)

                for d_row, d_col in neighbors:
                    new_row = row + d_row
                    new_col = col + d_col

                    # Check boundary and height conditions
                    if (0 <= new_row < rows and 
                        0 <= new_col < cols and 
                        (new_row, new_col) not in visited and 
                        heights[new_row][new_col] >= heights[row][col]):
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))

        # Perform BFS from ocean edges
        bfs(atl_q, atl_set)
        bfs(pac_q, pac_set)

        # Return cells reachable from both oceans
        return list(atl_set & pac_set)

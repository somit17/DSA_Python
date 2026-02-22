from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r: int, c: int) -> int:
            
            # Case 1: Out of bounds → contributes 1 to perimeter
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 1
            
            # Case 2: Water cell → contributes 1 to perimeter
            if grid[r][c] == 0:
                return 1
            
            # Case 3: Already visited land cell → contributes 0
            if (r, c) in visited:
                return 0
            
            # Case 4: New land cell → mark visited and check all 4 directions
            visited.add((r, c))
            
            # Calculate perimeter from all 4 neighbors
            perimeter = 0
            perimeter += dfs(r - 1, c)  # Up
            perimeter += dfs(r + 1, c)  # Down
            perimeter += dfs(r, c - 1)  # Left
            perimeter += dfs(r, c + 1)  # Right
            
            return perimeter
        
        # Find the first land cell to start DFS
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)
        
        return 0  # No island found
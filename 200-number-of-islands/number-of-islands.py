from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        def dfs(r, c):
            # Check boundaries and water
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            
            # Mark current land as visited
            grid[r][c] = "0"
            
            # Visit all 4 directions
            dfs(r+1, c)  # down
            dfs(r-1, c)  # up
            dfs(r, c+1)  # right
            dfs(r, c-1)  # left
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        
        return count

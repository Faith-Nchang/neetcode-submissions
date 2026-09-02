class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if (min(r, c) < 0 or r >= ROWS or c>= COLS or grid[r][c] == "0"):
                return
            
            grid[r][c] = "0"

            for row, col in dirs:
                dfs(r + row, c + col)
        
        c = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    c+=1
                    dfs(i, j)
        return c
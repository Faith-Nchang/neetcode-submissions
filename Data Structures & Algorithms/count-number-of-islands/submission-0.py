class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        counter = 0


        def dfs(row, col):
            if (
                min(row, col) < 0 or
                row >= ROWS or col >= COLS or
                grid[row][col] == "0"
             ):
                return 

            grid[row][col] = "0"

            for direction in directions:
                dfs(row + direction[0], col + direction[1])
                
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    counter += 1
        return counter


            

            
        
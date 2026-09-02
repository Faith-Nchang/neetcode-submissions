class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        
        def dfs(i, row, col):
            if i == len(word):
                return True
            if (min(row, col) < 0 or 
                row >= ROWS or 
                col >= COLS or 
                word[i] != board[row][col] or 
                (row, col) in visited):
               return False

            visited.add((row, col))
            res = (dfs(i+1, row+1, col) or
                    dfs(i+1, row-1, col) or
                    dfs(i+1, row, col+1) or
                    dfs(i+1, row, col-1)
            )
            visited.remove((row, col))
            return res
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(0, row, col):
                    return True
        return False
        
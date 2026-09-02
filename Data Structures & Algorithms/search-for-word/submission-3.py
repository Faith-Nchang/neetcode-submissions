class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        visited = set()

        def backtrack(index, row, col):
            if index == len(word):
                return True

            # fail
            if (min(row, col) < 0 or
                row >= ROWS or 
                col >= COLS or
                board[row][col] != word[index] or
                (row, col) in visited
            ):
                return False

            visited.add((row, col))
            path = (
                backtrack(index + 1, row + 1, col) or
                backtrack(index + 1, row - 1, col) or
                backtrack(index + 1, row, col + 1) or 
                backtrack (index + 1, row, col - 1)
            )
            visited.remove((row, col))
            return path
        for row in range(ROWS):
            for col in range(COLS):
                if backtrack(0, row, col):
                        return True

        return False
        
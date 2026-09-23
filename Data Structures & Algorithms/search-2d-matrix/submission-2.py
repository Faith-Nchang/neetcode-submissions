class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        r, c = 0, COLS - 1

        while r < ROWS and r >= 0 and c <  COLS and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target: 
                c -= 1
            else:
                r += 1

        return False
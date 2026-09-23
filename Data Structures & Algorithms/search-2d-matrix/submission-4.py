class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        top, bot = 0, ROWS - 1
        while top <= bot:
            r = (top + bot) // 2

            if target < matrix[r][0]:
                bot = r - 1
            elif target > matrix[r][-1]:
                top = r + 1
            else:
                break
        if not top <= bot:
            return False

        l, r = 0, COLS - 1
        row = matrix[(top + bot) // 2]

        while l <= r:
            mid = (l + r) // 2

            if row[mid] == target:
                return True
            elif row[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

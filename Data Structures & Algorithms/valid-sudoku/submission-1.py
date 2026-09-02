from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columnset = defaultdict(set)
        rowset = defaultdict(set)
        boxset = defaultdict(set)

        for r in range(9):
            for c in range(9):
                n = board[r][c]
                if n == ".":
                    continue
                box_r = r // 3
                box_c = c // 3
                if n in rowset[r] or n in columnset[c] or n in boxset[(box_r, box_c)]:
                    return False
                
                rowset[r].add(n)
                columnset[c].add(n)
                boxset[(box_r, box_c)].add(n)
        return True
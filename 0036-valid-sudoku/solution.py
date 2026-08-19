class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]
            
                if value == ".":
                    continue
            
                if value in row[r]:
                    return False
                elif value in col[c]:
                    return False
                elif value in box[3 * (r // 3) + (c // 3)]:
                    return False
                else:
                    row[r].add(value)
                    col[c].add(value)
                    box[3 * (r // 3) + (c // 3)].add(value)
        return True
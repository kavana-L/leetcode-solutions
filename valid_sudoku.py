class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen=set()
            for col in range(9):
                num=board[row][col]
                if num==".":
                    continue
                if num in seen:
                    return False
                seen.add(num)
        for col in range(9):
            seen=set()
            for row in range(9):
                num=board[row][col]
                if num==".":
                    continue
                if num in seen:
                    return False
                seen.add(num)
        for box_row in [0,3,6]:
            for box_col in [0,3,6]:
                seen=set()
                for row in range(box_row,box_row+3):
                    for col in range(box_col,box_col+3):
                        num=board[row][col]
                        if num==".":
                            continue
                        if num in seen:
                            return False
                        seen.add(num)
        return True

        
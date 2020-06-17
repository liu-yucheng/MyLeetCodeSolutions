from typing import List


class Solution:
    def validStr(self, string):
        numStrs = "123456789"
        existingNumStrs = ""
        for ch in string:
            if ch in numStrs:
                if ch in existingNumStrs:
                    return False
                else:
                    existingNumStrs += ch
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowStrs = ["".join(row) for row in board]
        print(f"{rowStrs}")
        for rowStr in rowStrs:
            strValid = self.validStr(rowStr)
            if not strValid:
                return False
        colStrs = ["".join([row[idx] for row in board]) for idx in range(9)]
        print(f"{colStrs}")
        for colStr in colStrs:
            strValid = self.validStr(colStr)
            if not strValid:
                return False
        boxStrs = []
        coordSets = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        for rowSet in coordSets:
            for colSet in coordSets:
                boxStr = ""
                for row in rowSet:
                    for col in colSet:
                        boxStr += board[row][col]
                boxStrs.append(boxStr)
        print(f"{boxStrs}")
        for boxStr in boxStrs:
            strValid = self.validStr(boxStr)
            if not strValid:
                return False
        return True

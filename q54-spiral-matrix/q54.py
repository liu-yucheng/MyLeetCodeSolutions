from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        maxRowNo = len(matrix) - 1
        if maxRowNo < 0:
            return []
        maxColNo = len(matrix[0]) - 1
        if maxColNo < 0:
            return []
        # print(f"maxRowNo:{maxRowNo}\tmaxColNo:{maxColNo}")
        maxElementCount = (maxRowNo + 1) * (maxColNo + 1)
        # print(f"maxElementCount:{maxElementCount}")
        result = []
        rowNo, colNo = 0, 0
        rowPad, colPad = 0, 0
        elementCount = 0
        direction = "right"
        spiralComplete = False
        while rowPad * 2 <= maxRowNo and colPad * 2 <= maxColNo:
            roundComplete = False
            while not roundComplete:
                # print(f"rowNo:{rowNo}\tcolNo:{colNo}\tdirection:{direction}")
                result.append(matrix[rowNo][colNo])
                if direction == "right" and colNo + colPad >= maxColNo:
                    direction = "down"
                elif direction == "down" and rowNo + rowPad >= maxRowNo:
                    direction = "left"
                elif direction == "left" and colNo - colPad <= 0:
                    direction = "up"
                elif direction == "up" and rowNo - rowPad - 1 <= 0:
                    direction = "right"
                    roundComplete = True
                if direction == "right":
                    colNo += 1
                elif direction == "down":
                    rowNo += 1
                elif direction == "left":
                    colNo -= 1
                elif direction == "up":
                    rowNo -= 1
                elementCount += 1
                if elementCount >= maxElementCount:
                    spiralComplete = True
                    break
            if spiralComplete:
                break
            rowPad += 1
            colPad += 1
        return result

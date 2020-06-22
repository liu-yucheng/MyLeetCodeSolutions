from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = [], []
        row = 0
        while row < len(matrix):
            # print(f'len(matrix):{len(matrix)}')
            col = 0
            while col < len(matrix[row]):
                # print(f'len(matrix[row]):{len(matrix[row])}')
                # print(f'row:{row}\tcol:{col}')
                if matrix[row][col] == 0:
                    if row not in rows:
                        rows.append(row)
                    if col not in cols:
                        cols.append(col)
                col += 1
            row += 1
        # print(f'rows:{rows}')
        # print(f'cols:{cols}')
        for row in rows:
            col = 0
            while col < len(matrix[row]):
                matrix[row][col] = 0
                col += 1
        for col in cols:
            row = 0
            while row < len(matrix):
                matrix[row][col] = 0
                row += 1

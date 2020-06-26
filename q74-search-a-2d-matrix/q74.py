from typing import List


class Solution:
    def convert(self, index, width):
        return [index // width, index % width]

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        if height == 0:
            return False
        width = len(matrix[0])
        if width == 0:
            return False
        length = height * width
        start, end = 0, length
        while end > start:
            mid = (start + end) // 2
            [row, col] = self.convert(mid, width)
            element = matrix[row][col]
            if target < element:
                end = mid
            elif target > element:
                start = mid + 1
            else:  # target == element
                return True
        return False

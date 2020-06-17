from typing import List


class Solution:
    def reverseRow(self, row):
        leftIndex = 0
        rightIndex = len(row) - 1
        while leftIndex < rightIndex:
            leftElement = row[leftIndex]
            rightElement = row[rightIndex]
            row[leftIndex] = rightElement
            row[rightIndex] = leftElement
            leftIndex += 1
            rightIndex -= 1

    def reverse(self, matrix):
        for row in matrix:
            self.reverseRow(row)

    def transpose(self, matrix):
        matrixHeight = len(matrix)
        if matrixHeight == 0:
            return
        matrixWidth = len(matrix[0])
        if matrixHeight != matrixWidth:
            return
        upIndex = 0
        upEndIndex = matrixHeight - 1
        while upIndex <= upEndIndex:
            leftIndex = 0
            leftEndIndex = matrixWidth - 1 - upIndex
            while leftIndex <= leftEndIndex:
                transposeRowIndex = matrixWidth - 1 - leftIndex
                transposeColumnIndex = matrixHeight - 1 - upIndex
                element = matrix[upIndex][leftIndex]
                transposeElement = \
                    matrix[transposeRowIndex][transposeColumnIndex]
                matrix[upIndex][leftIndex] = transposeElement
                matrix[transposeRowIndex][transposeColumnIndex] = element
                leftIndex += 1
            upIndex += 1

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.reverse(matrix)
        self.transpose(matrix)

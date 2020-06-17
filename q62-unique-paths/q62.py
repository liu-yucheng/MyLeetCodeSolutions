class Solution:
    def expand(self, resultMatrix, boundaryList):
        newBoundaryList = []
        for [rowIdx, colIdx] in boundaryList:
            if resultMatrix[rowIdx][colIdx] > 0:
                continue
            downVal = 0
            if rowIdx + 1 < len(resultMatrix):
                downVal = resultMatrix[rowIdx + 1][colIdx]
            rightVal = 0
            if colIdx + 1 < len(resultMatrix[0]):
                rightVal = resultMatrix[rowIdx][colIdx + 1]
            resultMatrix[rowIdx][colIdx] = downVal + rightVal
            if rowIdx - 1 >= 0:
                newBoundaryList.append([rowIdx - 1, colIdx])
            if colIdx - 1 >= 0:
                newBoundaryList.append([rowIdx, colIdx - 1])
        return newBoundaryList

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        resultMatrix = [[0 for _ in range(m)] for _ in range(n)]
        resultMatrix[n - 1][m - 1] = 1
        boundaryList = [[n - 2, m - 1], [n - 1, m - 2]]
        while len(boundaryList) > 0:
            boundaryList = self.expand(resultMatrix, boundaryList)
        return resultMatrix[0][0]

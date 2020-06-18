from typing import List


class Solution:
    def expand(self, result, boundary, obstacles, height, width):
        newBoundary = []
        for [row, col] in boundary:
            if obstacles[row][col] == 1:
                continue
            if result[row][col] > 0:
                continue
            down = 0
            if row < height - 1:
                down = result[row + 1][col]
            right = 0
            if col < width - 1:
                right = result[row][col + 1]
            result[row][col] = down + right
            if row > 0:
                newBoundary.append([row - 1, col])
            if col > 0:
                newBoundary.append([row, col - 1])
        return newBoundary

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height = len(obstacleGrid)
        if height <= 0:
            return 0
        width = len(obstacleGrid[0])
        if width <= 0:
            return 0
        # print(f"height:{height}\twidth:{width}")
        if height == 1:
            if 1 in obstacleGrid[0]:
                return 0
            else:
                return 1
        if width == 1:
            if [1] in obstacleGrid:
                return 0
            else:
                return 1
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        result = [[0 for _ in range(width)] for _ in range(height)]
        result[height - 1][width - 1] = 1
        boundary = [[height - 2, width - 1], [height - 1, width - 2]]
        while len(boundary) > 0:
            # print(f"boundary:{boundary}")
            boundary = self.expand(
                result, boundary, obstacleGrid, height, width
            )
        return result[0][0]

from typing import List


class Solution:
    def expand(self, result, grid, boundary, height, width):
        newBoundary = []
        for [row, col] in boundary:
            if result[row][col] >= 0:
                continue
            down = None
            if row < height - 1:
                down = result[row + 1][col]
            right = None
            if col < width - 1:
                right = result[row][col + 1]
            if down is None and right is None:
                result[row][col] = grid[row][col]
            elif down is not None and right is None:
                result[row][col] = grid[row][col] + down
            elif down is None and right is not None:
                result[row][col] = grid[row][col] + right
            else:
                result[row][col] = grid[row][col] + min(down, right)
            if row > 0:
                newBoundary.append([row - 1, col])
            if col > 0:
                newBoundary.append([row, col - 1])
        return newBoundary

    def minPathSum(self, grid: List[List[int]]) -> int:
        height = len(grid)
        if height <= 0:
            return 0
        width = len(grid[0])
        if width <= 0:
            return 0
        # print(f"width:{width}\theight:{height}")
        result = [[-1 for _ in range(width)] for _ in range(height)]
        boundary = [[height - 1, width - 1]]
        while len(boundary) > 0:
            # print(f"result:{result}")
            # print(f"boundary:{boundary}")
            boundary = self.expand(result, grid, boundary, height, width)
        return result[0][0]

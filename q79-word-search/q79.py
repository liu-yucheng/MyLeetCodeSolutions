from typing import List


class Solution:
    def backtrack(self, board, word, row, col, height, width):
        if len(word) == 0:
            return True
        if row < 0 or row > height - 1:
            return False
        if col < 0 or col > width - 1:
            return False
        if board[row][col] == word[0]:
            board[row][col] = ''
            newWord = word[1:]
            result = False
            result |= self.backtrack(
                board, newWord, row - 1, col, height, width
            )
            result |= self.backtrack(
                board, newWord, row + 1, col, height, width
            )
            result |= self.backtrack(
                board, newWord, row, col - 1, height, width
            )
            result |= self.backtrack(
                board, newWord, row, col + 1, height, width
            )
            if result is True:
                return result
            board[row][col] = word[0]
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        if height == 0:
            return False
        width = len(board[0])
        if width == 0:
            return False
        for row in range(height):
            for col in range(width):
                if self.backtrack(board, word, row, col, height, width):
                    return True
        return False

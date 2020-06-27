from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        for idx in range(n):
            result += [(elem + 2 ** idx) for elem in result[::-1]]
        return result

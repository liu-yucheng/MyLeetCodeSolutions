class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numStrList = [str(i) for i in range(1, n + 1)]
        curIdxSize = 1
        for i in range(1, n + 1):
            curIdxSize *= i
        curIdxProd = k - 1
        result = ""
        for i in range(n, 1, -1):
            curIdxSize //= i
            curIdx = curIdxProd // curIdxSize
            result += numStrList.pop(curIdx)
            curIdxProd %= curIdxSize
        result += numStrList.pop()
        return result

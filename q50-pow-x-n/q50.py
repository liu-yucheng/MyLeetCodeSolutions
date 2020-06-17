class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0
        if n == 0.0:
            return 1.0
        nSign = 1
        if n < 0:
            nSign = -1
            n = -n
        prodList = []
        for exp in range(32):
            if exp == 0:
                prodList.append(x)
            else:
                prodList.append(prodList[exp - 1] * prodList[exp - 1])
        result = 1.0
        for idx, prod in enumerate(prodList):
            mask = 1 << idx
            xHasProd = n & mask != 0
            if xHasProd:
                result *= prod
        if nSign == -1:
            result = 1 / result
        return result

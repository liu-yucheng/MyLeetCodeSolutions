class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def intBound(v):  # v: value
            if v < -0x8000_0000:
                v = -0x8000_0000
            if v > 0x7fff_ffff:
                v = 0x7fff_ffff
            return v

        if divisor == 0:
            return 0x7fff_ffff
        if dividend == 0:
            return 0
        if divisor == 1:
            return intBound(dividend)
        if divisor == -1:
            return intBound(-dividend)
        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor
        result = 0
        for iter in range(30, -1, -1):
            pow = 1 << iter
            prod = divisor << iter
            if prod == 0:
                prod = 0x7fff_ffff
            if prod <= dividend:
                result |= pow
                dividend -= prod
                if dividend == 0:
                    break
        if sign == -1:
            result = -result
        return intBound(result)

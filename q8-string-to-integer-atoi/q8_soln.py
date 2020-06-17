class Solution(object):
    def myAtoi(self, s):
        if len(s) == 0:
            return 0
        i = 0  # index
        while i < len(s) and s[i] == ' ':
            i += 1
        if i >= len(s) or s[i] not in "-+1234567890":
            return 0
        elif s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            sign = 1
            i += 1
        else:
            sign = 1
        f = i  # from
        while i < len(s) and s[i] in "1234567890":
            i += 1
        t = i  # to
        intmin = -1 * 2 ** 31
        intmax = 2 ** 31 - 1
        r = 0  # result
        i2 = f  # index 2
        while i2 < t:
            d = ord(s[i2]) - 0x30
            if sign == 1:
                r += d
            else:
                r -= d
            i2 += 1
            if i2 < t:
                r *= 10
            if r < intmin:
                r = intmin
                break
            elif r > intmax:
                r = intmax
                break
        return r

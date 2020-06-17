class Solution(object):
    def intToRoman(self, num):
        if num < 1:
            return "I"  # roman numeral for 1
        elif num > 3999:
            return "MMMCMXCIX"  # roman numeral for 3999
        n1000 = num // 1000  # number of thousands
        num -= n1000 * 1000
        n100 = num // 100  # number of hundreds
        num -= n100 * 100
        n10 = num // 10  # number of tens
        num -= n10 * 10
        n1 = num

        def romanString(d, c1, c5, c10):
            # d: digit, c1: character for 1, c5: character for 5,
            # c10: character for 10
            if d == 9:
                return c1 + c10
            elif d == 4:
                return c1 + c5
            else:
                rs = ""  # roman string
                if d >= 5:
                    rs += c5
                    d -= 5
                rs += c1 * d
                return rs
        r = ""  # result
        r += 'M' * n1000
        r += romanString(n100, 'C', 'D', 'M')
        r += romanString(n10, 'X', 'L', 'C')
        r += romanString(n1, 'I', 'V', 'X')
        return r

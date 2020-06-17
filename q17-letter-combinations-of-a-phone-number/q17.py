class Solution(object):
    def letterCombinations(self, digits):
        dt = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }  # digit table

        def expand(c, d):  # c: combinations, d: digit
            if d not in dt.keys():
                return
            if len(c) == 0:
                for ch in dt[d]:  # ch: character
                    c.append(ch)
                return
            r = []  # result
            for e in c:  # e: element
                for ch in dt[d]:  # ch: character
                    s = e + ch  # string
                    r.append(s)
            c.clear()
            c += r

        r = []  # result
        for d in digits:  # d: digit
            expand(r, d)
        return r

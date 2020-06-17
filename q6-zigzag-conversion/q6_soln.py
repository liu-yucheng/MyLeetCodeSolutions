class Solution(object):
    def convert(self, s, numRows):
        r = ["" for _ in range(numRows)]  # result
        i = 0  # index
        row = 0
        go_up = False
        while i < len(s):
            r[row] += s[i]
            if go_up:
                row -= 1
            else:
                row += 1
            i += 1
            if row > numRows - 1:
                go_up = True
                if numRows <= 1:
                    row = 0
                else:
                    row = numRows - 2
            elif row < 0:
                go_up = False
                if numRows <= 1:
                    row = 0
                else:
                    row = 1
        return "".join(r)

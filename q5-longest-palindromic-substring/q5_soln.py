class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ""
        elif len(s) == 1:
            return s
        r = ""  # result
        i2f = 0  # index 2 * from
        i2c = 0  # index 2 * center
        i2t = 0  # index 2 * to
        rc = ""  # result candidate
        while i2c // 2 < len(s):
            if i2c % 2 == 0:
                i2f = i2c - 2
                i2t = i2c + 2
                rc = str(s[i2c // 2])
            else:
                i2f = i2c - 1
                i2t = i2c + 1
                if i2f // 2 < 0 or \
                        i2t // 2 >= len(s) or \
                        s[i2f // 2] != s[i2t // 2]:
                    i2c += 1
                    continue
                rc = str(s[i2f // 2] + s[i2t // 2])
                i2f -= 2
                i2t += 2
            while i2f // 2 >= 0 and \
                    i2t // 2 < len(s) and \
                    s[i2f // 2] == s[i2t // 2]:
                rc = s[i2f // 2] + rc + s[i2t // 2]
                i2f -= 2
                i2t += 2
            if len(rc) > len(r):
                r = rc
            i2c += 1
        return r

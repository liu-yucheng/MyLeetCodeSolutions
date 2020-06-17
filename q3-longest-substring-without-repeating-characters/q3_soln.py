class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sl = len(s)  # string length
        if sl <= 1:
            return sl
        f = 0  # from
        t = 1  # to
        r = 0  # result
        while t < sl:
            rc = 0  # result candidate
            if t == sl - 1:
                rc = t + 1 - f
            if s[t] in s[f:t]:
                rc = t - f
                while s[t] in s[f:t] and f < t:
                    f += 1
            if rc > r:
                r = rc
            t += 1
        return r

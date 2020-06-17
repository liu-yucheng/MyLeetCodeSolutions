class Solution(object):
    def maxArea(self, height):
        r = 0  # result
        hls = [e for e in height]  # height list sorted
        hls = list(set(sorted(height)))[::-1]
        for h in hls:
            if len(height) * h < r:
                continue
            i = 0  # index
            while height[i] < h:
                i += 1
            f = i  # from
            i = len(height) - 1
            while height[i] < h:
                i -= 1
            t = i  # to
            a = (t - f) * h
            if a > r:
                r = a
        return r

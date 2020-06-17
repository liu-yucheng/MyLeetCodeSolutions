# implementing the official solution: 2 pointers approach
class Solution(object):
    def maxArea(self, height):
        r = 0  # result
        i1 = 0  # result
        i2 = len(height) - 1  # result
        while i1 != i2:
            h1 = height[i1]
            h2 = height[i2]
            a = (i2 - i1) * min(h1, h2)
            if a > r:
                r = a
            if h1 <= h2:
                i1 += 1
            else:
                i2 -= 1
        return r

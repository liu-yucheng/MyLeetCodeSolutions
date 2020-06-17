from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n <= 0:
            return []
        elif n == 1:
            return [[1]]
        r = [[0 for _ in range(n)] for _ in range(n)]  # result
        ri, ci = 0, 0  # ri: row index; ci: column index
        sp = 0  # spiral padding
        d = 'r'  # direction (r: right)
        i = 1  # iterator
        nSq = n ** 2  # n-Squared
        while i <= nSq:
            rc = False  # round complete
            while not rc:
                # print(f"ri:{ri}\tci:{ci}")
                r[ri][ci] = i
                if d == 'r' and ci + sp >= n - 1:
                    d = 'd'
                elif d == 'd' and ri + sp >= n - 1:  # (d: down)
                    d = 'l'
                elif d == 'l' and ci - sp <= 0:  # (l: left)
                    d = 'u'
                elif d == 'u' and ri - sp <= 1:  # (u: up)
                    rc = True
                    d = 'r'
                if d == 'r':
                    ci += 1
                elif d == 'd':
                    ri += 1
                elif d == 'l':
                    ci -= 1
                elif d == 'u':
                    ri -= 1
                i += 1
                if i > nSq:
                    break
            sp += 1
        return r

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        r = []  # result
        for cn in range(n):  # closure number
            for lf in self.generateParenthesis(cn):  # left
                for rt in self.generateParenthesis(n - cn - 1):  # right
                    r.append("({}){}".format(lf, rt))
        return r

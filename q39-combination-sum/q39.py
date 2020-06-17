from typing import List


class Solution:
    def expand(self, combinations, candidates, target):
        rl = []  # result less
        re = []  # result equal
        if len(combinations) == 0:
            for e in candidates:
                if e < target:
                    rl.append([e])
                elif e == target:
                    re.append([e])
        else:
            for c in combinations:  # c: combination
                # print(f"expand: c: {c}")
                soc = sum(c)  # sum of combination
                for e in candidates:  # e: element
                    if e < c[-1]:
                        continue
                    ns = soc + e  # new sum
                    if ns < target:
                        nc = [e2 for e2 in c]  # nc: new combination
                        nc.append(e)
                        rl.append(nc)
                    elif ns == target:
                        nc = [e2 for e2 in c]  # nc: new combination
                        nc.append(e)
                        re.append(nc)
        return [rl, re]

    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        ac = [e for e in candidates if e <= target]  # actual candidates
        if len(ac) == 0:
            return []
        ac.sort()
        # print(f"ac: {ac}")
        maxL = target // ac[0] + 1  # maximum length
        # print(f"maxL: {maxL}")
        r = []  # result
        currC = []
        for currL in range(1, maxL + 1):  # iteration counter
            [rl, re] = self.expand(currC, candidates, target) \
                    # rl: result less, re: result equal
            # print(f"currL: {currL}\n\tcurrC: {currC}\n\trl: {rl}\n\tre: {re}")
            currC = rl
            r += re
            if len(rl) == 0:
                break
        return r

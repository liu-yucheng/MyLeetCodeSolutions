from typing import List


class Solution:
    @classmethod
    def expand(cls, combs, cands, tar):
        # combs: combinations
        # cands: candidates
        # tar: target
        rl = []  # result (less)
        re = []  # result (equal)
        if len(combs) == 0:
            for idx, cand in enumerate(cands): \
                    # idx: index, cand: candidate
                if idx > 0 and cand == cands[idx - 1]:
                    continue
                if cand < tar:
                    rl.append([cand])
                elif cand == tar:
                    re.append([cand])
        else:
            for comb in combs:  # comb: combination
                combSum = sum(comb)  # combination sum
                for idx, cand in enumerate(cands): \
                        # idx: index, cand: candidate
                    if idx > 0 and cand == cands[idx - 1]:
                        continue
                    if cand < comb[-1]:
                        continue
                    if comb.count(cand) >= cands.count(cand):
                        continue
                    newSum = combSum + cand
                    if newSum < tar:
                        newComb = [elem for elem in comb]  # new combination
                        newComb.append(cand)
                        rl.append(newComb)
                    elif newSum == tar:
                        newComb = [elem for elem in comb]  # new combination
                        newComb.append(cand)
                        re.append(newComb)
        return [rl, re]

    def combinationSum2(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        aC = [e for e in candidates if e <= target]  # actual candidates
        if len(aC) == 0:
            return []
        aC.sort()
        maxL = 0  # maximum length
        curS = 0  # current sum
        for e in aC:  # e: element
            curS += e
            maxL += 1
            if curS > target:
                break
        # print(f"maxL: {maxL}")
        curC = []  # current combinations
        r = []  # result
        for curL in range(maxL):  # current length
            [rl, re] = Solution.expand(curC, aC, target)
            # print(f"curL: {curL}\n\tcurC: {curC}\n\trl: {rl}\n\tre: {re}")
            curC = rl
            r += re
            if len(rl) == 0:
                break
        return r

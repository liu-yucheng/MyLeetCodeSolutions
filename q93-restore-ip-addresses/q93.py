from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        length = len(s)
        if length == 0:
            return []
        subresults = [[] for _ in range(length)]
        idx = length - 1
        while idx >= 0:
            if idx == length - 1:
                character = s[idx]
                subresults[idx].append([character])
            else:
                probList = subresults[idx + 1]
                for prob in probList:
                    character = s[idx]
                    byte = prob[0]
                    if len(prob) < 4 and (
                            len(byte) <= 1 or
                            (len(byte) > 1 and byte[0] != '0')
                    ):
                        newProb = prob[:]
                        newProb.insert(0, character)
                        subresults[idx].append(newProb)
                    newByte = character + byte
                    newVal = int(newByte)
                    if newVal <= 255:
                        newProb = prob[:]
                        newProb[0] = newByte
                        subresults[idx].append(newProb)
            idx -= 1
        result = []
        for prob in subresults[0]:
            byte = prob[0]
            if len(prob) == 4 and (
                    len(byte) <= 1 or
                    (len(byte) > 1 and byte[0] != '0')
            ):
                result.append('.'.join(prob))
        result.sort()
        return result

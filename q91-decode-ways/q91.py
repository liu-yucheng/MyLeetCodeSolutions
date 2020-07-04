class Solution:
    def numDecodings(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        subresult = [0 for _ in range(length + 1)]
        subresult[-1] = 1
        last = int(s[-1])
        if last != 0:
            subresult[-2] = 1
        for idx in range(length - 2, -1, -1):
            first = int(s[idx])
            if first == 0:
                continue
            firstTwo = int(s[idx: idx + 2])
            if firstTwo <= 26:
                subresult[idx] = subresult[idx + 1] + subresult[idx + 2]
            else:
                subresult[idx] = subresult[idx + 1]
        return subresult[0]

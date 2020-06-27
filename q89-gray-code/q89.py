from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n <= 0:
            return [0]
        count0 = {}
        count1 = {}
        value = 0
        result = []
        maxCount = 2 ** (n - 1)
        # print(f'maxCount:{maxCount}')
        for idx in range(n):
            count0[idx] = 0
            count1[idx] = 0
        while True:
            result.append(value)
            # print(f'result:{result}')
            for idx in range(n):
                mask = 1 << idx
                bit1 = value & mask != 0
                if bit1:
                    count1[idx] += 1
                else:
                    count0[idx] += 1
            newValue = value
            for idx in range(n):
                mask = 1 << idx
                bit1 = value & mask != 0
                candidate = newValue ^ mask
                if candidate in result:
                    continue
                if bit1:
                    if count0[idx] < maxCount:
                        newValue ^= mask
                        break
                else:
                    if count1[idx] < maxCount:
                        newValue ^= mask
                        break
            if newValue == value:
                break
            value = newValue
        return result

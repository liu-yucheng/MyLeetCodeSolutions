from typing import List


class Solution:
    def expand(self, result, nums):
        newResult = []
        for comb in result:
            for num in nums:
                if num <= comb[-1]:
                    continue
                newComb = [elem for elem in comb]
                newComb.append(num)
                newResult.append(newComb)
        return newResult

    def combine(self, n: int, k: int) -> List[List[int]]:
        if k <= 0:
            return []
        nums = [iter for iter in range(1, n + 1)]
        if k >= n:
            return [nums]
        result = [[iter] for iter in range(1, n - k + 2)]
        for _ in range(k - 1):
            # print(f'result:{result}')
            result = self.expand(result, nums)
        return result

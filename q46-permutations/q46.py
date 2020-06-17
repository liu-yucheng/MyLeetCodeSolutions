from typing import List


class Solution:
    def expand(self, permList, numList):
        if len(permList) == 0:
            result = []
            for num in numList:
                newPerm = [num]
                if newPerm not in result:
                    result.append(newPerm)
            return result
        result = []
        for perm in permList:
            for num in numList:
                if perm.count(num) >= numList.count(num):
                    continue
                newPerm = [e for e in perm]
                newPerm.append(num)
                if newPerm not in result:
                    result.append(newPerm)
        return result

    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for _ in range(len(nums)):
            result = self.expand(result, nums)
        return result

from typing import List


class Solution:
    def expand(self, subresult, nums):
        if len(subresult) == 0:
            return [[elem] for elem in nums]
        newSubesult = []
        for subset in subresult:
            for elem in nums:
                if elem <= subset[-1]:
                    continue
                newSubset = subset[:]
                newSubset.append(elem)
                newSubesult.append(newSubset)
        return newSubesult

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        subresult = []
        for _ in range(len(nums)):
            subresult = self.expand(subresult, nums)
            result += subresult
        return result

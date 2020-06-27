from typing import List


class Solution:
    def expand(self, subresult, nums):
        newSubresult = []
        for subset in subresult:
            for elem in nums:
                if subset and subset[-1] > elem:
                    continue
                if subset.count(elem) >= nums.count(elem):
                    continue
                newSubset = subset[:]
                newSubset.append(elem)
                if newSubset not in newSubresult:
                    newSubresult.append(newSubset)
        return newSubresult

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]
        subresult = [[]]
        for _ in range(len(nums)):
            subresult = self.expand(subresult, nums)
            result += subresult
        return result

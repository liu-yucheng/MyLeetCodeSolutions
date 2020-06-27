from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]
        subresult = []
        for idx in range(len(nums)):
            if idx > 0 and nums[idx - 1] == nums[idx]:
                subresult = [subset + [nums[idx]] for subset in subresult]
            else:
                subresult = [subset + [nums[idx]] for subset in result]
            result += subresult
        return result

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 2:
            return length
        [idx1, idx2, idx3] = [0, 1, 2]
        remove = False
        while idx3 < length:
            while idx3 < length and \
                    nums[idx1] == nums[idx2] and \
                    nums[idx2] == nums[idx3]:
                nums.pop(idx3)
                length = len(nums)
            idx3 += 1
            idx2 = idx3 - 1
            idx1 = idx3 - 2
        return length

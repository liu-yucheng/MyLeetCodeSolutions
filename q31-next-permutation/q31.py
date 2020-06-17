import numpy
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        idx = len(nums) - 1
        while idx > 0 and nums[idx - 1] >= nums[idx]:
            idx -= 1
        if idx == 0:
            idx2 = len(nums) - 1
            while idx < idx2:
                nums[idx] ^= nums[idx2]
                nums[idx2] ^= nums[idx]
                nums[idx] ^= nums[idx2]
                idx += 1
                idx2 -= 1
        else:
            swapIdx1 = idx - 1
            swapIdx2 = idx
            while idx < len(nums):
                if nums[idx] > nums[swapIdx1] and nums[idx] <= nums[swapIdx2]:
                    swapIdx2 = idx
                idx += 1
            nums[swapIdx1] ^= nums[swapIdx2]
            nums[swapIdx2] ^= nums[swapIdx1]
            nums[swapIdx1] ^= nums[swapIdx2]
            idx = swapIdx1 + 1
            idx2 = len(nums) - 1
            while idx < idx2:
                nums[idx] ^= nums[idx2]
                nums[idx2] ^= nums[idx]
                nums[idx] ^= nums[idx2]
                idx += 1
                idx2 -= 1

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        idx = 0
        curr0Start, curr0End = None, None
        while idx <= len(nums) - 1:
            if curr0Start is None and nums[idx] <= 0:
                curr0Start = idx
            if curr0Start is not None and nums[idx] > 0:
                curr0End = idx
            if idx == len(nums) - 1:
                curr0End = idx
            if curr0Start is not None and curr0End is not None:
                curr0Len = curr0End - curr0Start
                idx2 = curr0Start - 1
                minDist = curr0Len + 1
                canPass = False
                while True:
                    if idx2 < 0:
                        break
                    if canPass:
                        break
                    if nums[idx2] >= minDist:
                        canPass = True
                    idx2 -= 1
                    minDist += 1
                if not canPass:
                    return False
                curr0Start, curr0End = None, None
            idx += 1
        return True

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        left = 0
        right = len(nums)
        mid = -1
        idxTarget = -1
        while left < right:
            mid = (left + right) // 2
            # print(f"left:{left}\tmid:{mid}\tright:{right}")
            numMid = nums[mid]
            if target < numMid:
                right = mid
            elif target > numMid:
                left = mid + 1
            else:  # target == numMid
                idxTarget = mid
                break
        if idxTarget == -1:
            return [-1, -1]
        left = 0
        right = idxTarget
        idxTargetLeft = -1
        if left == right:
            idxTargetLeft = right
        while left < right:
            mid = (left + right) // 2
            # print(f"left:{left}\tmid:{mid}\tright:{right}")
            numMid = nums[mid]
            if target < numMid:  # this should not happen
                right = mid
            elif target > numMid:
                left = mid + 1
            else:  # target == numMid
                right = mid
            if left == right:
                idxTargetLeft = right
                break
        left = idxTarget
        right = len(nums)
        idxTargetRight = -1
        if left == right:
            idxTargetRight = right - 1
        while left < right:
            mid = (left + right) // 2
            # print(f"left:{left}\tmid:{mid}\tright:{right}")
            numMid = nums[mid]
            if target < numMid:
                right = mid
            elif target > numMid:  # this should not happen
                left = mid + 1
            else:  # target == numMid
                left = mid + 1
            if left == right:
                idxTargetRight = right - 1
                break
        return [idxTargetLeft, idxTargetRight]

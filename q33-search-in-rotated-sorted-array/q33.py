from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lf = 0
        rt = len(nums) - 1
        while (lf <= rt):
            mid = (lf + rt) // 2
            if target == nums[mid]:
                return mid
            if nums[lf] <= nums[mid]:
                if target >= nums[lf] and target <= nums[mid]:
                    rt = mid - 1
                else:
                    lf = mid + 1
            else:
                if target >= nums[mid] and target <= nums[rt]:
                    lf = mid + 1
                else:
                    rt = mid - 1
        return -1

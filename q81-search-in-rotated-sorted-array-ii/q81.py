from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums)
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[start]:
                if nums[mid] < target:
                    start = mid + 1
                else:
                    if nums[start] <= target:
                        end = mid
                    else:
                        start = mid + 1
            elif nums[mid] < nums[end - 1]:
                if nums[mid] > target:
                    end = mid
                else:
                    if nums[end - 1] >= target:
                        start = mid + 1
                    else:
                        end = mid
            else:
                return target in nums
        return False

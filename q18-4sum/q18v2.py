from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        i1 = 0  # index 1
        i2 = 1  # index 2
        i3 = len(nums) - 2  # index 3
        i4 = len(nums) - 1  # index 4
        r = []  # result
        while i1 < len(nums) - 3:
            if i1 > 0 and nums[i1] == nums[i1 - 1]:
                i1 += 1
                continue
            i4 = len(nums) - 1
            while i1 + 1 < i4 - 1:
                if i4 < len(nums) - 1 and nums[i4] == nums[i4 + 1]:
                    i4 -= 1
                    continue
                i2 = i1 + 1
                i3 = i4 - 1
                while i2 < i3:
                    s = nums[i1] + nums[i2] + nums[i3] + nums[i4]  # sum
                    if s == target:
                        r.append([nums[i1], nums[i2], nums[i3], nums[i4]])
                    if s <= target:
                        e2 = nums[i2]  # element 2
                        while i2 < i3 and nums[i2] == e2:
                            i2 += 1
                    if s >= target:
                        e3 = nums[i3]  # element 3
                        while i2 < i3 and nums[i3] == e3:
                            i3 -= 1
                e4 = nums[i4]  # element 4
                i4 -= 1
            e1 = nums[i1]  # element 1
            i1 += 1
        r2 = []  # result 2
        for e in r:  # e: element
            if e not in r2:
                r2.append(e)
        return r2

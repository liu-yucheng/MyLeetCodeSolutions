from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = {}
        for element in nums:
            if element in counts.keys():
                counts[element] += 1
            else:
                counts[element] = 1
        idx = 0
        for color in [0, 1, 2]:
            if color in counts.keys():
                for _ in range(counts[color]):
                    nums[idx] = color
                    idx += 1

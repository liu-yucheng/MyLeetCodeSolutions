from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if len(intervals) <= 1:
            return intervals
        index = 0
        while index < len(intervals) - 1:
            currInterval = intervals[index]
            nextInterval = intervals[index + 1]
            if currInterval[1] >= nextInterval[0]:
                currInterval[1] = max(currInterval[1], nextInterval[1])
                del intervals[index + 1]
            else:
                index += 1
        return intervals

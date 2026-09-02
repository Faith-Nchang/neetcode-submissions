from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort by end time (this is the greedy trick)
        intervals.sort(key=lambda x: x[1])

        res = 0
        nonOverlap = [0]   # store indices of non-overlapping intervals

        for i in range(1, len(intervals)):
            # check overlap with the last non-overlapping interval
            if intervals[i][0] < intervals[nonOverlap[-1]][1]:
                # overlap -> must remove this one
                res += 1
            else:
                # no overlap -> keep it
                nonOverlap.append(i)

        return res

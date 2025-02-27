#435. Non-overlapping Intervals
#Medium
#problem statement:   https://leetcode.com/problems/non-overlapping-intervals/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res, pre_end = 0, intervals[0][1]

        for  (start, end) in intervals[1:]:
            if pre_end <= start: pre_end = end
            else:
                res += 1
                pre_end = min(pre_end, end)
     
        return res
            

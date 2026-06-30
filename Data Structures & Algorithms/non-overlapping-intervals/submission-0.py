class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        count = 0
        prev_end = intervals[0][1]

        for interval in intervals[1:]:
            if prev_end > interval[0]:
                count +=1 # overlap found
                prev_end = min(prev_end, interval[1]) # why minimum?
            else:
                prev_end = interval[1]

        return count
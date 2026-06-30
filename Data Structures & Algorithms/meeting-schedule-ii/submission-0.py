"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda i: i.start)
        min_heap = []
        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                # min_heap[0]: interval end time < next start
                # min_heap is not empty 
                # we are only pushing end times into the heap
                heapq.heapreplace(min_heap, interval.end)
            else:
                heapq.heappush(min_heap, interval.end)

        return len(min_heap)

        
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda i:i.start)
        ends = []
        for i in intervals:
            start = i.start
            end = i.end
            if ends and ends[0] <= start:
                heapq.heappop(ends)
            heapq.heappush(ends,end)
        return len(ends)
        
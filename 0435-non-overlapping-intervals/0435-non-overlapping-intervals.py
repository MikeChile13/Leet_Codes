class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        last_interval = 0
        count = 0
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[last_interval][1]:
                count += 1
            else:
                last_interval = i

        # print(intervals)
        return count
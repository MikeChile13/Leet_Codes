class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        prev_end,prev_start = intervals[0]
        merged = []
        for i in range(1,len(intervals)):
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i][0] = min(intervals[i][0],intervals[i-1][0])
                intervals[i][1] = max(intervals[i][1],intervals[i-1][1])
            else:
                merged.append(intervals[i-1])
        merged.append(intervals[-1])
        return merged

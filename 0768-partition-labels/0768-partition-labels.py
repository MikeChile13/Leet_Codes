class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals = dict()

        for i,char in enumerate(s):
            if char not in intervals:
                intervals[char] = [i,i]
            intervals[char][1] = i

        intervals = list(intervals.values())
        # print(intervals)
        merged = [intervals[0]]

        for i in range(1,len(intervals)):
            if intervals[i][0] <= merged[-1][1]:
                merged[-1][0] = min(merged[-1][0],intervals[i][0])
                merged[-1][1] = max(merged[-1][1],intervals[i][1])
            else:
                merged.append(intervals[i])
                
        # print(merged)
        return [end - start + 1 for start,end in merged]
            
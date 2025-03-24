class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ranges = []
        for time in timeSeries:
            ranges.append([time,time+duration-1])
        merged = []
        print(ranges)
        for i in range(1,len(ranges)):
            if ranges[i][0] <= ranges[i-1][1]:
                ranges[i][0] = min(ranges[i][0],ranges[i-1][0])
                ranges[i][1] = max(ranges[i][1],ranges[i-1][1])
            else:
                merged.append(ranges[i-1])
        merged.append(ranges[-1])
        print(merged)
        ans = 0
        for start, end in merged:
            ans += end - start + 1

        return ans
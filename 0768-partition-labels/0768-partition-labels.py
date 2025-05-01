class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ranges = defaultdict()
        for index,char in enumerate(s):
            if char not in ranges:
                ranges[char] = [index,index]
            else:
                ranges[char][1] = index
        # print(ranges)
        ranges = sorted(list(ranges.values()))
        print(ranges)
        res = []
        start,end = ranges[0]
        for i in range(1,len(ranges)):
            if ranges[i][0] > end:
                res.append([start,end])
                start,end = ranges[i]
            else:
                end = max(ranges[i][1],end)
                start = min(ranges[i][0],start)

        res.append([start,end])
        
        return [end - start+1 for start,end in res]
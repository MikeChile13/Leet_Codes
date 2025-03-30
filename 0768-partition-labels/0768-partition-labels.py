class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ends = dict()

        for i,char in enumerate(s):
            ends[char] = i

       
        res = []
        prev_start = 0
        prev_end = ends[s[0]]


        for i in range(len(s) - 1):
            if i == prev_end:
                res.append(i - prev_start + 1)
                prev_start = i + 1
                prev_end = ends[s[i + 1]]
            prev_end = max(ends[s[i]], prev_end)

        res.append(prev_end - prev_start + 1)
        return res
            
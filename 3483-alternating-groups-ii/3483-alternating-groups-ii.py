class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        count = 0
        res = 0
        n = len(colors)
        for i in range(1,n+k):
            if colors[i%n] != colors[(i-1)%n]:
                count+=1
            else:
                count = 1
            if count >= k:
                res +=1
        # print(colors)
        return res
        
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:k])
        count = 0
        res = 0
        for i in range(1,len(colors)):
            if colors[i] != colors[i-1]:
                count+=1
            else:
                count = 1
            if count >= k:
                res +=1
        # print(colors)
        return res
        
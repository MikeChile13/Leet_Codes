class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        satcount=0
        i=0
        j=0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                satcount+=1
                i+=1
            j+=1
        return satcount
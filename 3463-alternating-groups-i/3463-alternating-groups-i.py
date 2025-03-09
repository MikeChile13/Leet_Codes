class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        alts = 0 
        n = len(colors)
        for i in range(n):
            if colors[(i+1)%n] == colors[(i-1)%n] != colors[i]:
                alts += 1
        return alts




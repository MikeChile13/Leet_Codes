class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        power = 0
        ans = 0
        for i in range(len(columnTitle)-1,-1,-1):
            ans += (ord(columnTitle[i])-64)* pow(26,power) 
            power += 1 
        
        return ans
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        letters = {}
        for i in range(1,27):
            letters[chr(i + 64)] = i
        
        power = 0
        ans = 0
        for i in range(len(columnTitle)-1,-1,-1):
            ans += letters[columnTitle[i]] * pow(26,power) 
            power += 1 
        print(letters)
        return ans
class Solution:
    def minimumLength(self, s: str) -> int:
        
        freqs = [0]*26
        #For each of the characters take the center.
        #if there are two centers add two
        #else add one.

        #if count is even, two centers.
        #if count is odd, one center.
        for char in s:
            freqs[ord(char)-97]+=1
        res = 0
        for val in freqs:
            if val==0:
                continue
            elif val %2 == 1:
                res+=1
            else:
                res+=2
        return res

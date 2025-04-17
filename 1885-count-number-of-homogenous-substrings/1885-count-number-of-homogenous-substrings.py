class Solution:
    def countHomogenous(self, s: str) -> int:
        count = 0
        window = 1
        modulo = 1_000_000_007
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                window += 1
            else:
                if window > 1:
                    count = ( count + window * (window + 1) // 2) % modulo 
                else:
                    count = ( count + 1 ) % modulo
                # print(window)
                window = 1
        if window > 1:
            count = ( count + window * (window + 1) // 2) % modulo 
        else:
            count = ( count + 1 ) % modulo

        return count
                

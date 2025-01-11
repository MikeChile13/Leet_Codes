class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False
        if n == k:
            return True
        freq = [0]*26
        oddCount = 0
        for char in s:
            freq[ord(char)-97]+=1
        for count in freq:
            if count % 2 == 1:
                oddCount+=1
        return oddCount <= k
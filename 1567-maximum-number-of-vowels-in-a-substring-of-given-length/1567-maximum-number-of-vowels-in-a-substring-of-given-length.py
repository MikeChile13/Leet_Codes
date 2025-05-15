class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if not s or k>len(s):
            return 0
        vowels = 'aeiouAEIOU'
        maxc = count = 0
        for i in range(k):
            if s[i] in vowels:
                count+=1
        maxc = count
        for i in range(k,len(s)):
            count += s[i] in vowels
            count -= s[i-k] in vowels
            maxc = max(maxc,count)
        return maxc


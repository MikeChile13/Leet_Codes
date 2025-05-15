class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        n = len(s)
        r = [''] * n
        for word in s:
            r[int(word[-1])-1] = word[:-1]
        return ' '.join(r)
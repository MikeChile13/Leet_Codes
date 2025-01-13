class Solution:
    def minimumLength(self, s: str) -> int:
        freqs = Counter(s)
        res = 0
        for val in freqs.values():
            if val % 2 == 1:
                res+= 1
            else:
                res+=2
        return res

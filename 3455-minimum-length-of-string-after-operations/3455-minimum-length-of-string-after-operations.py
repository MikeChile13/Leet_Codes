class Solution:
    def minimumLength(self, s: str) -> int:
        freqs = Counter(s)
        #For each of the characters take the center.
        #if there are two centers add two
        #else add one.

        #if count is even, two centers.
        #if count is odd, one center.
        res = 0
        for val in freqs.values():
            if val % 2 == 1:
                res+= 1
            else:
                res+=2
        return res

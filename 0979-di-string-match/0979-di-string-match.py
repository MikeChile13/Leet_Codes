class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        d = len(s)
        i = 0
        p = 0
        res = []
        while p < len(s):
            if s[p] == 'D':
                res.append(d)
                d-=1
            else:
                res.append(i)
                i+=1
            p+=1
        if s[p-1] == 'D':
            res.append(d)
        else:
            res.append(i)
        return res
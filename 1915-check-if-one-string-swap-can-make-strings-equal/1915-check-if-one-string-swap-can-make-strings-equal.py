class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        positions = 0
        idx=[]
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                positions+=1
                idx.append(i)
        if not positions:
            return True
        if positions != 2:
            return False
        if s1[idx[0]] == s2[idx[1]] and s2[idx[0]] == s1[idx[1]]:
            return True
        return False 
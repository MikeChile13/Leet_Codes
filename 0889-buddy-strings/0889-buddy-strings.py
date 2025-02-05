class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        slen,glen = len(s),len(goal)
        if slen != glen:
            return False
        freqs = defaultdict(int)
        positions = 0
        idx = []
        for i in range(slen):
            freqs[s[i]]+=1
            if s[i] != goal[i]:
                positions+=1
                idx.append(i)
        if not positions:
            if all(v == 1 for v in freqs.values()):
                return False
            return True
        if positions != 2:
            return False
        if s[idx[0]] == goal[idx[1]] and s[idx[1]] == goal[idx[0]]:
            return True
        return False 

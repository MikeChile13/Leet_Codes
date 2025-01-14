class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = defaultdict()
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]]=1
            else:
                return s[i]
        return s[0]

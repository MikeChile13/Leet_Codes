class Solution:
    def checkString(self, s: str) -> bool:
        last_a = 0
        first_b = 0
        for i in range(len(s)):
            if not first_b and s[i] == 'b':
                first_b = i
            if s[i] == 'a':
                last_a = i
        if not last_a:
            return True
        if not first_b and s[0]!='b':
            return True
        if last_a < first_b:
            return True
        return False
                
        
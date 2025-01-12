class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:

        n = len(s)

        if n % 2 == 1:
            return False

        opens = []
        unlocked = []

        for i in range(n):
            if locked[i] == '0':
                unlocked.append(i)
            elif s[i] == "(":
                opens.append(i)
            elif s[i] == ")":
                if opens:
                    opens.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
        
        while opens and unlocked and opens[-1] < unlocked[-1]:
            opens.pop()
            unlocked.pop()
        if opens:
            return False
        return True

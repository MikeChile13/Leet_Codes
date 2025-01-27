class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        s = s.lstrip()
        if not s:
            return 0
        i = 0
        ans = 0
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
        while i < len(s) and s[i].isnumeric():
            ans = ans * 10 + int(s[i])
            i+=1
        if not ans:
            return 0
        ans *= sign
        if ans < -2**31:
            return -2**31
        elif ans > 2**31-1:
            return 2**31-1
        else:
            return ans

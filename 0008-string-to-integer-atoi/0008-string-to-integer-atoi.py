class Solution:
    def myAtoi(self, s: str) -> int:
        minv,maxv = -2**31,2**31 - 1
        sign = 1
        ans = []
        chars = s.lstrip()
        print(chars)
        if not chars:
            return 0
        length = len(chars)
        if chars[0] == '-':
            sign = -1
            i = 1
        elif chars[0] == '+':
            i = 1
        else:
            i = 0
        while i < length and chars[i].isnumeric():
            ans.append(chars[i])
            i+=1

        print(chars,ans)
        if not ans:
            return 0
        ans = int(''.join(ans)) * sign
        if ans < minv:
            return minv
        elif ans > maxv:
            return maxv
        else:
            return ans

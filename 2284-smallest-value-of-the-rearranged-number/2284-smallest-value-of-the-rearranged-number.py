class Solution:
    def smallestNumber(self, num: int) -> int:
        if not num: return 0
        sign = 1 if num > 0 else 0
        vals = []
        if not sign:
            num = -num
        while num:
                vals.append(num%10)
                num //= 10
        n = len(vals)
        if sign:
            vals.sort()
            
            for i in range(n-1,-1,-1):
                if vals[i] == 0 and i < n-1:
                    vals[0],vals[i+1] = vals[i+1],vals[0]
                    break
            sign = vals[0]
            for i in range(1,n):
                sign = sign*10 + vals[i]
            return sign
            
        else:
            vals.sort(reverse = True)
            val = vals[0]
            for i in range(1,n):
                val = val*10 + vals[i]

            return -val

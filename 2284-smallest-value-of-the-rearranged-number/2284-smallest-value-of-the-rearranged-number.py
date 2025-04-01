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

        else:
            vals.sort(reverse = True)
            val = vals[0]

        ans = ''
        print(vals)
        for val in vals:
            ans += str(val)
        
        return int(ans) if sign else int('-'+ans)
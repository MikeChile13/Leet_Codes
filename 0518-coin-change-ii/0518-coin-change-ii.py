class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}
        def takeskip(i,sumv):
            if (i,sumv) in memo:
                return memo[(i,sumv)]

            if sumv == amount:
                return 1
            if sumv > amount or i >= n:
                return 0

            take = takeskip(i,sumv + coins[i])

            skip = takeskip(i+1,sumv)
            memo[(i,sumv)] = take + skip
            return memo[(i,sumv)]
        
        return takeskip(0,0)
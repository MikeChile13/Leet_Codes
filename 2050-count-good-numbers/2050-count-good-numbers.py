class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 1_000_000_007
        ans = 1
        even = math.ceil(n/2)
        odd = math.floor(n/2)

        ans = ans * pow(4,odd,MOD)
        ans = ( ans * pow(5,even,MOD) ) % MOD
        
        return ans
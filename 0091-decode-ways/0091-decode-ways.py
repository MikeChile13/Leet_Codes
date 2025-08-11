class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        memo = {}

        def CountWays(i):

            if i in memo:
                return memo[i]
            if i == n:
                return 1
            if s[i] == '0':
                return 0

            ans = 0

            for j in range(i,min(i + 2, n)):
                v = int(s[i:j+1])

                if 1 <= v <= 26:
                    ans += CountWays(j+1)
            memo[i] = ans

            return memo[i]
        return CountWays(0)
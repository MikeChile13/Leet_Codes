class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = defaultdict(int)
        cache = [-1 for _ in range(n+1)]
        def f(n):
            if n < 0:
                return 0

            if n == 0:
                return 1

            # if n not in memo:
                # memo[n] = f(n-1) + f(n-2)
            if cache[n] == -1:
                cache[n] = f(n-1) + f(n-2)

            return cache[n]

        return f(n)
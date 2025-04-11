class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0
        while n:
            rem = n % k
            n  //= k
            res += rem
        return res
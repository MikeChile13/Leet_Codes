class Solution:
    def isUgly(self, n: int) -> bool:

        while n > 1 and not n%2:
            n //= 2
        while n > 1 and not n%3:
            n //= 3
        while n > 1 and not n%5:
            n //= 5
        return n == 1
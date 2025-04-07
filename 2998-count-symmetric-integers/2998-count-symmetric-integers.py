class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        def isSymmetric(num: int) -> bool:
            s = str(num)
            n = len(s)
            if n%2:
                return False
            leftSum = 0
            rightSum = 0
            for i in range(n//2):
                leftSum += int(s[i])
                rightSum += int(s[n-i-1])
            return leftSum == rightSum
        result = 0
        for i in range(low,high+1):
            if isSymmetric(i):
                result += 1

        return result
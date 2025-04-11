class Solution:
    def isSymmetric(self, num: str) -> bool:
        n = len(num)
        if n % 2:
            return False
        left = 0
        right = 0
        for i in range(n//2):
            left += int(num[i])
            right += int(num[n-i-1])
        return left == right
        
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low,high+1):
            count += self.isSymmetric(str(num))

        return count

        
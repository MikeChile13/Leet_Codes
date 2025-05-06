class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return floor(math.sqrt(num))**2 == num
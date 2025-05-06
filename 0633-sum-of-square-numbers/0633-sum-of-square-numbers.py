class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start = 0
        end = int(math.sqrt(c))
        while start <= end:
            sumv = start**2 + end**2
            if sumv == c:
                return True
            elif sumv > c:
                end -= 1
            else:
                start += 1
        return False
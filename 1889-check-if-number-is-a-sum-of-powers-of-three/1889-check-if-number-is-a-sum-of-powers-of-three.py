import math
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        max_x = int(math.log(n,3))
        while max_x >= 0:
            val = 3**max_x
            max_x -= 1
            if val > n:
                continue
            n -= val

        # print(n)

        return not n
        
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1 = str(num1)
        num2 = str(num2)
        num3 =  str(num3)
        num1 = '0'* (4 - len(num1)) + num1
        num2 = '0'* (4 - len(num2)) + num2
        num3 = '0'* (4 - len(num3)) + num3
        key = ''
        for i in range(4):
            key += min(num1[i],num2[i],num3[i])
        return int(key)
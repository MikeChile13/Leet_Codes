class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        num = [i for i in range(1,n+1)]
        position = 0
        while len(num) > 1:
            index = ( position + k - 1 ) % len(num)
            num.pop(index)
            position = index
        return num[-1]


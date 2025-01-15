# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def search(low,high):
            if low > high:
                return None
            mid = low + (high - low)//2
            v = guess(mid)
            if v == 0:
                return mid
            elif v < 0:
                return search(low,mid-1)
            else:
                return search(mid+1,high)
        return search(1,n)

            

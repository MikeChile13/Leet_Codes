class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        return [] if num%3 else  [num//3 -1, num//3, num//3 + 1]
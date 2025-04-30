class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evens = 0
        for num in nums:
            c = 0
            while num:
                c+= 1
                num //=10
            if c % 2 == 0:
                evens += 1
        return evens
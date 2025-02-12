class Solution:
    def digiSum(self, num:int) -> int:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num//=10
        return digit_sum
    def maximumSum(self, nums: List[int]) -> int:
        seen = {}
        res = -1

        for num in nums:
            digit_sum = self.digiSum(num)
            if digit_sum in seen:
                res = max(res, num + seen[digit_sum])
                seen[digit_sum] = max(num,seen[digit_sum])
            else:
                seen[digit_sum] = num
        return res
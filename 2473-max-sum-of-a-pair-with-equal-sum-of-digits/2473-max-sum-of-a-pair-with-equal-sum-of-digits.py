class Solution:
    def digiSum(self, num:int) -> int:
        return sum([int(val) for val in list(str(num))])
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
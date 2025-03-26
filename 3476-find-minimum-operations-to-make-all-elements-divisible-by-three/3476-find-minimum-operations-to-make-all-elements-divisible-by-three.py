class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # opps = 0
        # for num in nums:
        #     opps += min(num%3, 3 - num%3)
        # return opps
        ans = 0
        for num in nums:
            ans += num%3 != 0
        return ans
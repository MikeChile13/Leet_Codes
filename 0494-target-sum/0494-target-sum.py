class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.ans = 0
        n = len(nums)
        memo = {}
        def dp(i,sumv):
            if i == n:
                if sumv == target:
                    return 1
                return 0
            if (i,sumv) in memo:
                return memo[(i,sumv)]
            if i+1 <= n:
                memo[(i,sumv)] = dp(i+1,sumv + nums[i]) + dp(i+1,sumv - nums[i])
                return memo[(i,sumv)]
            return 0
        return dp(0,0)
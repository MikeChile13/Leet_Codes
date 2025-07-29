class Solution:
    def rob(self, nums: List[int]) -> int:
        #take and not take, when take skip
        n = len(nums)
        # @lru_cache(None)
        memo = {}

        def dp(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            take = nums[i] + dp(i+2)
            skip = dp(i+1)

            memo[i] = max(take,skip)

            return memo[i]

        return dp(0)
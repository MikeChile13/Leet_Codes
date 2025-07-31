class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False
        target = s // 2
        n = len(nums)
        self.found = False
        memo = {}
        def backtrack(i, total):
            if (i,total) in memo:
                return memo[(i,total)]
            if total == target:
                return True
            if i >= n or total > target:
                return False
            memo[(i,total)] = backtrack(i+1,total + nums[i])  or backtrack(i+1,total)
            return memo[(i,total)]
        return backtrack(0,0)

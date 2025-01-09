class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum,left = 0,0
        n = len(nums)
        diff = n+1
        for right in range(n):
            window_sum+=nums[right]
            while window_sum >= target:
                diff = min(diff,right-left+1)
                window_sum-=nums[left]
                left+=1
        return diff if diff <= n else 0

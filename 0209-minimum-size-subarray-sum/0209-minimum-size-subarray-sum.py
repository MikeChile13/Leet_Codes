class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSubarray = float('inf')

        runsum = 0
        i = 0
        j = 0
        n = len(nums)
        while j < n:
            runsum += nums[j]
            while runsum >= target:
                minSubarray = min(minSubarray,j - i + 1)
                runsum -= nums[i]
                i += 1
            j += 1
        return minSubarray if minSubarray != float('inf') else 0
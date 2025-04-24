class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #sliding window
        
        n = len(nums)

        sumv = 0
        left = 0

        size = float('inf')

        for right in range(n):
            sumv += nums[right]

            while sumv >= target:

                size = min(size,right - left + 1)
                sumv -= nums[left]
                left += 1
            
        return size if size != float('inf') else 0


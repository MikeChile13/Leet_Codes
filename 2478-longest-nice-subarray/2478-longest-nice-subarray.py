class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        xor = 0
        sumv = 0
        left,right = 0,0
        ans = 0
        #if the and of any group of number s is equal to the sum, the and is equal to 0.
        #from that sliding window is implemented.
        while right < len(nums):
            xor ^= nums[right]
            sumv += nums[right]
            while sumv != xor:#shrinking the window when there is a conflict
                sumv -= nums[left]
                xor ^= nums[left]
                left += 1
            ans = max(ans,right - left + 1)
            right += 1
        return ans


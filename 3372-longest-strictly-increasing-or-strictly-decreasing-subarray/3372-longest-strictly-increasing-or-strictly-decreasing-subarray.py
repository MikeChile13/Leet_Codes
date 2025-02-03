class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        inc_count, dec_count = 1,1
        res = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc_count+=1
                dec_count = 1
            elif nums[i] < nums[i-1]:
                dec_count+=1
                inc_count = 1
            else:
                inc_count,dec_count= 1,1
        
            res = max(res,inc_count,dec_count)
        return res

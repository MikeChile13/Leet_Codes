class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc, dec = -1,51
        inc_count, dec_count = 0,0
        res = 0
        
        for i in range(len(nums)):
            if nums[i] > inc:
                inc_count+=1
                dec_count = 1
            elif nums[i] < dec:
                dec_count+=1
                inc_count = 1
            else:
                inc_count,dec_count= 1,1
            inc,dec = nums[i],nums[i]
            res = max(res,inc_count,dec_count)
        return res

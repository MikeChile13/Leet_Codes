class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sumv = nums[0]
        res  = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                sumv+=nums[i]
            else:
                sumv = nums[i]
            res = max(res,sumv)
        return res
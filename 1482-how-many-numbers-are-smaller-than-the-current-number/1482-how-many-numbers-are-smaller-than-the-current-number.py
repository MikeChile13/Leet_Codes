class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] == nums[i]:
                    continue
                res[i] += (nums[j] < nums[i])
                
        return res

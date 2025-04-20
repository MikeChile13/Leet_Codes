class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        size = 1
        curr_max = nums[0]
        for i in range(1,len(nums)):
            if nums[i] >= curr_max:
                size += 1
                curr_max = nums[i]
            # print(size,curr_max,less)
        return size
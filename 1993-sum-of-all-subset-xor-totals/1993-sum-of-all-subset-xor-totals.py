class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        running_or = 0
        for num in nums:
            running_or |= num
        return running_or << len(nums)-1
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums)//2]
        sumv = 0
        for val in nums:
            sumv += abs(val - median)

        return sumv
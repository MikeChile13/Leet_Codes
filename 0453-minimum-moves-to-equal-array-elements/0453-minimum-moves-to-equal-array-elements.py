class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # val = min(nums)
        # sumv = 0
        # for num in nums:
        #     sumv += abs(num - val)
        # return sumv
        return sum(nums) - ( min(nums) * len(nums) )
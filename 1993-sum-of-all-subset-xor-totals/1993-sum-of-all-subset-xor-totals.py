class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        def backtrack(index,xor):
            if index >= n:
                return xor

            not_take = backtrack(index + 1,xor)

            take = backtrack(index + 1,xor^nums[index])
            
            return not_take + take

        return backtrack(0,0)
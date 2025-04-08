class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        while len(nums) > 0:

            if len(nums) == len(set(nums)):
                return operations

            nums = nums[3:]
            operations += 1

        return operations
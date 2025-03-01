class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        write_index = 0
        for i in range(n-1):
            if not nums[i]:
                continue

            if nums[i] == nums[i+1]:
                nums[i] *=2
                nums[i+1] = 0

            nums[write_index] = nums[i]
            if write_index != i:
                nums[i] = 0
            write_index += 1

        if nums[-1] and write_index < n - 1:
            nums[write_index] = nums[-1]
            nums[-1] = 0

        return nums
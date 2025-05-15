class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z,o = 0,0
        n = len(nums)

        for num in nums:
            if num == 0:
                z += 1
            elif num == 1:
                o += 1

        for i in range(0,z):
            nums[i] = 0
        for i in range(z,z + o):
            nums[i] = 1
        for i in range(z + o, n):
            nums[i] = 2
            

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        i,j = 0,0
        groups = 1
        while i <= j < len(nums):
            if nums[j] - nums[i] > k:
                groups+=1
                i = j
            else:
                j+=1
        return groups
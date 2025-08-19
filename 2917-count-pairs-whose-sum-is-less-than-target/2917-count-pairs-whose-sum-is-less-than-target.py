class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lessPairs = 0
        for i in range(n):
            for j in range(i+1,n):
                lessPairs += (nums[i] + nums[j] < target)
        return lessPairs

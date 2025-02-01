class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prev = nums[0]&1
        for i in range(1,len(nums)):
            current = nums[i]&1
            if prev == current:
                return False
            prev = current
        return True
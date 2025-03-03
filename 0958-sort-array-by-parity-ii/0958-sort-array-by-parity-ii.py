class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left,right = 0,1
        i = True
        while right < n and left < n:
            if nums[left] %2 == 0:
                left += 2
            elif nums[right] %2 == 1:
                right +=2
            else:
                nums[right],nums[left] = nums[left],nums[right]

        return nums
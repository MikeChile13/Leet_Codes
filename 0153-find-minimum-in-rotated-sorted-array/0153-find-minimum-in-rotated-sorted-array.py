class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right = 0,len(nums)-1

        while left < right:
            
            mid = left + (right - left)//2
            # If mid element is greater than the rightmost element, min is on the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
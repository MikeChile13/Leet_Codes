class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        n = len(nums)

        if nums[0] > 0 or nums[-1] < 0:
            return n

        left,right = 0,n-1
        #find first positive
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] <= 0:
                left = mid + 1
            else:
                right = mid - 1
        #count positives
        pos = n - left

        #find last negative using range 0 to first positive
        right = left-1
        left = 0

        #find last negative
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] >= 0:
                right = mid - 1
            else:
                left = mid + 1
        # print(pos,right)
        
        return max(pos,right+1)
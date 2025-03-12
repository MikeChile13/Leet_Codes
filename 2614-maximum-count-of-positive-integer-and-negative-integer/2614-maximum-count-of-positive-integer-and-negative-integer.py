class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        left,right = 0,n-1

        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] <= 0:
                left = mid + 1
            else:
                right = mid - 1
        pos = n - left

        left,right = 0,n-1

        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] >= 0:
                right = mid - 1
            else:
                left = mid + 1
        # print(pos,right)
        return max(pos,right+1)
class Solution:
    def binarySearch(self,left,right):
        while left <= right:
            mid = left + (right - left)//2
            if self.nums[mid] == self.target:
                return mid
            elif self.nums[mid] > self.target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        return self.binarySearch(0,len(nums)-1)
class Solution:
    def binarySearch(self,left,right):
        mid = left + (right - left)//2
        if left > right:
            return -1
        if self.nums[mid] == self.target:
            return mid
        elif self.nums[mid] < self.target:
            return self.binarySearch(mid+1,right)
        else:
            return self.binarySearch(left,mid-1)
    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        return self.binarySearch(0,len(nums)-1)
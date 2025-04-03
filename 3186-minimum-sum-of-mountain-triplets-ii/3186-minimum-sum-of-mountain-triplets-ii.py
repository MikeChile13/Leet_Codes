class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        min_left = [0]*n
        res = float('inf')
        min_left[0],min_left[-1] = -1,-1
        smallest_left = nums[0]

        
        for i in range(1,n):
            min_left[i] = smallest_left
            smallest_left = min(smallest_left,nums[i])
        smallest_right = nums[-1]
        for i in range(n-2,0,-1):
            if min_left[i] < nums[i] > smallest_right:
                res = min(res,min_left[i]+smallest_right+nums[i])
            smallest_right = min(smallest_right,nums[i])

        return -1 if res == float('inf') else res
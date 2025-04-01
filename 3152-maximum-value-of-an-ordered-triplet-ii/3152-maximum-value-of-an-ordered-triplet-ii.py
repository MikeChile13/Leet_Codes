class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        left,right = [0] * n, [0] * n
        left[0] = nums[0]
        right[-1] = nums[-1]
        for i in range(1,n):
            left[i] = max(left[i-1],nums[i])
            right[n-i-1] = max(right[n-i],nums[n-i-1])
        print(left,right)
        max_score = 0
        for i in range(1,n-1):
            max_score = max(max_score,( left[i-1] - nums[i] ) * right[i + 1])
        return max_score
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        right = [0] * n
        right[-1] = nums[-1]
        for i in range(1,n):
            right[n-i-1] = max(right[n-i],nums[n-i-1])
        # print(left,right)
        max_score = 0
        max_left = nums[0]
        for i in range(1,n-1):
            max_score = max(max_score,( max_left - nums[i] ) * right[i + 1])
            max_left = max(max_left,nums[i])
        return max_score
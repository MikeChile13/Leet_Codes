class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda x: x[0])
        merged = []
        for i in range(1,len(nums)):
            if nums[i][0]<= nums[i-1][1]:
                nums[i][0] = nums[i-1][0]
                nums[i][1] = max(nums[i][1],nums[i-1][1])
            else:
                merged.append(nums[i-1])
        merged.append(nums[-1])
        # print(merged)
        ans = 0
        for start,end in merged:
            ans += end - start + 1
        return  ans

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        c = 0
        ans = 0
    
        for right in range(len(nums)):
            if not nums[right]:
                c += 1
            else:
                ans += (c * (c + 1)//2 )
                # print(ans)
                c = 0
        if c:
            ans += (c * (c + 1)//2 )
        
        return ans
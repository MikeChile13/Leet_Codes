class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maps = {}
        ans = 0
        for i in range(len(nums)):
            if nums[i] not in maps:
                maps[nums[i]] = float('inf')
        for i in range(len(nums)):        
            if nums[i]+1 in maps:
                maps[nums[i]+1] = nums[i]
        for key in maps.keys():
            length = 1
            val = key
            if val+1 not in maps:
                while maps[val] != float('inf'):
                    length+=1
                    val = maps[val]
            ans = max(ans,length)
        return ans
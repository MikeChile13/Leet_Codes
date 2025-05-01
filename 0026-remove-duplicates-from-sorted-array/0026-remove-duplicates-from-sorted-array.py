
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
        seen = sorted(list(seen))
        for i in range(len(seen)):
            nums[i] = seen[i]
        
        return len(seen)
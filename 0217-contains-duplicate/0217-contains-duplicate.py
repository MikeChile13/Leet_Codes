class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = defaultdict(int)
        for i in range(len(nums)):
            counts[nums[i]]+=1
            if counts[nums[i]]>1:
                return True
        return False

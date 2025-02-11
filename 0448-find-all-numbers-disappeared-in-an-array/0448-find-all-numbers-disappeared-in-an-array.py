class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        map = defaultdict(int)
        for i in range(len(nums)):
            map[i+1]+=1
        for i in range(len(nums)):
            if nums[i] in map:
                del map[nums[i]]
        return list(map.keys())

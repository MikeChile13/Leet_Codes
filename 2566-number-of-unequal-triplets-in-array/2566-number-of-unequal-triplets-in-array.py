class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        frequencies = Counter(nums)
        res = 0
        left = 0
        right = len(nums)

        for freq in frequencies.values():
            right -= freq
            res += left * freq * right
            left += freq
        
        return res
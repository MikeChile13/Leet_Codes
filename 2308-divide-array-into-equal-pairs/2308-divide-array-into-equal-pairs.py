class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        Freqs = Counter(nums)
        length = len(nums)

        for key,freq in Freqs.items():
            if freq % 2:
                return False
        return True
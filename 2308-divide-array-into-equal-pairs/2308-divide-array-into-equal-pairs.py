class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = {}
        odds = 0
        for num in nums:
            freq[num] = freq.get(num,0) + 1
            if freq[num] % 2:
                odds += 1
            else:
                odds -= 1

        return not odds
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        def rev(num: int) -> int:
            return int(str(num)[::-1])

        n = len(nums)
        good_pairs = 0

        pairings = defaultdict(int)

        for i,number in enumerate(nums):
            revDiff = ( number - rev(number) ) % MOD
            good_pairs = ( good_pairs + pairings.get(revDiff,0) ) % MOD
            pairings[revDiff]+=1

        return good_pairs
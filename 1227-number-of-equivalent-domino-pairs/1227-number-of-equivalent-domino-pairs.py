class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs = defaultdict(int)
        for pair in dominoes:
            pairs[tuple(sorted(pair))] += 1

        count = 0

        for value in pairs.values():
            count += value * (value - 1)//2

        return count
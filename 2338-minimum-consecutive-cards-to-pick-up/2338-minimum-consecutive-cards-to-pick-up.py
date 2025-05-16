class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        maps = dict()
        min_dist = float('inf')
        for i in range(len(cards)):
            if cards[i] in maps:
                min_dist = min(min_dist,i-maps[cards[i]]+1)
                maps[cards[i]] = i
                continue
            maps[cards[i]] = i
        return min_dist if min_dist != float('inf') else -1
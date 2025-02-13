class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-val for val in piles]
        heapq.heapify(max_heap)
        while k:
            val = ceil(-heapq.heappop(max_heap)/2)
            heapq.heappush(max_heap,-val)
            k-=1
        return -sum(max_heap)
            
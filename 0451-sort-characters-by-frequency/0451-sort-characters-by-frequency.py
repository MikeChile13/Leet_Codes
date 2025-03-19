class Solution:
    def frequencySort(self, s: str) -> str:
        occurs = Counter(s)
        max_heap = []
        for c,v in occurs.items():
                heapq.heappush(max_heap,(-v,c))
        res = ''
        while max_heap:
            v, c = heapq.heappop(max_heap)
            res += c * -v
        
        return res

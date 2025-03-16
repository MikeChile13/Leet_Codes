class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        sim = [0]*len(ranks)
        min_heap = []
        for i in range(len(ranks)):
            heapq.heappush(min_heap,(ranks[i],i))
        
        for _ in range(cars):
            _,index = heapq.heappop(min_heap)
            sim[index] +=1

            r = ranks[index]
            n = sim[index]+1
            heapq.heappush(min_heap,(r*(n**2),index))
        ans = 0
        for i,val in enumerate(sim):
            ans = max(ans,ranks[i]*(val**2))
        return ans
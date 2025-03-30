class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        min_cost = cost[0]
        for i in range(len(cost)):
            if cost[i] < min_cost:
                min_cost = cost[i]
            cost[i] = min_cost
        return cost
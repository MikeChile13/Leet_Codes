class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        vals = sorted(costs,key=lambda x: x[0]-x[1])
        cost = 0

        for i in range(len(vals)//2):
            cost += (vals[i][0] + vals[-i-1][1])

        return cost
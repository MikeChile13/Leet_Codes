class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        # def possible(i):
        #     move = n
        #     tank = 0
        #     while move:
        #         tank += gas[i] - cost[i]
        #         if tank < 0:
        #             return False
        #         i = (i+1)%n
        #         move -= 1
        #     return True

        # for i in range(n):
        #     if gas[i] < cost[i]:
        #         continue
        #     if possible(i):
        #         return i

        # return -
            
        total = 0      # total gain across whole loop
        tank = 0       # current tank while scanning
        start = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total += gain
            tank += gain

            if tank < 0:      # fail here, skip to i+1
                start = i + 1
                tank = 0

        return start if total >= 0 else -1
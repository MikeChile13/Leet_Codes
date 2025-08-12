class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = {}
        def optimize(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            
            take = questions[i][0] +optimize(i+questions[i][1]+1)
            skip = optimize(i+1)
            memo[i] = max(take,skip)
            return memo[i]
        
        return optimize(0)
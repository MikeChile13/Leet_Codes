class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n

        for i in range(n-1, -1, -1):
            points, jumps = questions[i]
            take = points + dp[jumps + i + 1] if jumps + i + 1 < n else points
            not_take = dp[i+1] if i + 1 < n else 0
            dp[i] = max(take, not_take)

        return dp[0]
        
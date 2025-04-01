class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        for i in range(n-1, -1, -1):
            points, jumps = questions[i]
            take = points + questions[jumps + i + 1][0] if jumps + i + 1 < n else points
            not_take = questions[i+1][0] if i + 1 < n else 0
            questions[i][0] = max(take, not_take)

        return questions[0][0]
        
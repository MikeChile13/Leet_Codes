class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        left_sum = 0
        right_sum = sum(cardPoints[n - k:])
        max_score = right_sum

        for i in range(1, k + 1):
            left_sum += cardPoints[i - 1]
            right_sum -= cardPoints[n - k + i - 1]
            max_score = max(max_score, left_sum + right_sum)

        return max_score

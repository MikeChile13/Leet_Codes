class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        @cache
        def forward_tracking(index):
            if index >= n:
                return 0
                
            take = questions[index][0] + forward_tracking(index + questions[index][1] + 1)
            skip = forward_tracking(index + 1)

            return max(take,skip)
        
        return forward_tracking(0)

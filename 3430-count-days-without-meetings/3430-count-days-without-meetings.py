class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:x[0])

        free_days = 0
        prev_start,prev_end = meetings[0]
        free_days += prev_start - 1
        for i in range(1,len(meetings)):
            curr_start,curr_end = meetings[i]
            if curr_start > prev_end:
                free_days += curr_start - prev_end - 1
                prev_end = curr_end
            else:
                prev_end = max(curr_end,prev_end)

        free_days += days - prev_end
        return free_days
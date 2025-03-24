class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        repeat = 0
        for i in range(len(timeSeries)-1):
            difference = timeSeries[i+1] - timeSeries[i]
            if difference < duration:
                repeat += duration - difference

        return len(timeSeries) * duration - repeat
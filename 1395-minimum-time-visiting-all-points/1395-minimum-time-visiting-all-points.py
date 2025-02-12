class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        distance = 0
        n = len(points)
        
        for i in range(n-1):
            (x1,y1),(x2,y2) = points[i],points[i+1]
            distance+= max(abs(x1-x2),abs(y1-y2))
        
        return distance


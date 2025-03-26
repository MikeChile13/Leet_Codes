class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        rectangles.sort()
        count = 0
        prev_end = rectangles[0][2]
        for i in range(1,len(rectangles)):
            start, end = rectangles[i][0],rectangles[i][2]
            if start < prev_end:
                prev_end = max(prev_end,end)
            else:
                count += 1
                prev_end = end
        if count >= 2:
            return True

        count = 0
        rectangles.sort(key=lambda x: x[1])
        prev_end = rectangles[0][3]
        for i in range(1,len(rectangles)):
            start, end = rectangles[i][1],rectangles[i][3]
            if start < prev_end:
                prev_end = max(prev_end,end)
            else:
                count += 1
                prev_end = end
        return count >= 2


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        def inrange(i,j):
            if 0 <= i < m and 0 <= j < n:
                return True
            return False
        
        neighbours = [(-1,-1),(1,1),(-1,1),(1,-1),(1,0),(0,1),(0,-1),(-1,0)]

        res = [[0 for _ in range(n)] for _ in range(m)]
        # print(res)

        def Smoothing(i,j):
            average = 1
            sumv = img[i][j]
            for x,y in neighbours:
                if inrange(i+x,j+y):
                    average += 1
                    sumv += img[i+x][j+y]
            res[i][j] = sumv//average
            return

        for i in range(m):
            for j in range(n):
                Smoothing(i,j)
        return res
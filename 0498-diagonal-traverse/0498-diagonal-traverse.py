class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        switch = 0

        res = [mat[0][0]]
        for i in range(1,m):
            # print(switch)
            row = []
            x,y = i,0
            while x >= 0 and y < n:
                row.append(mat[x][y])
                x -= 1
                y += 1
            if switch:
                res.extend(row)
            else:
                res.extend(row[::-1])
            switch ^= 1
        for i in range(1,n):
            row = []

            x,y = m-1, i
            while x >= 0 and y < n:
                row.append(mat[x][y])
                x -= 1
                y += 1
            
            if switch:
                res.extend(row)
            else:
                res.extend(row[::-1])
            switch ^= 1

        return res
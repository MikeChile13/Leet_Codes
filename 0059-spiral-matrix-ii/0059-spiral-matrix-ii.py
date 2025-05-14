class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        left,right = 0,len(matrix[0])
        top,bottom = 0,len(matrix)
        val = 1
        while left < right and top < bottom:
            for i in range(left,right):
                matrix[top][i] = val
                val += 1
            top +=1
            for i in range(top,bottom):
                matrix[i][right-1] = val
                val += 1
            right-=1
            if not (left < right and top < bottom):
                break
            for i in range(right-1,left-1,-1):
                matrix[bottom-1][i] = val
                val += 1
            bottom -=1
            for i in range(bottom-1,top-1,-1):
                matrix[i][left] = val
                val += 1
            left+=1
        return matrix
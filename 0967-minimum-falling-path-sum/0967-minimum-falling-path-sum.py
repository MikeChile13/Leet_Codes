class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1,n):
            for j in range(n):
                a,c = float('inf'),float('inf')
                if 0 <= j-1 < n:
                    a = matrix[i-1][j-1]
                if 0 <= j+1 < n:
                    c = matrix[i-1][j+1]
                matrix[i][j] += min(matrix[i-1][j],a,c)
        
        min_path_sum = float('inf')
        # print(matrix)
        for j in range(n):
            min_path_sum = min(min_path_sum,matrix[n-1][j])
        return min_path_sum

                

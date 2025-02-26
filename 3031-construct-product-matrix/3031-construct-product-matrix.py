class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n,m = len(grid),len(grid[0])
        prefix = 1
        mod = 12345
        result = [[1] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                result[i][j] = prefix
                prefix = (prefix * grid[i][j]) % mod
        
        postfix = 1
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                result[i][j] = (result[i][j] * postfix ) % mod
                postfix = (postfix * grid[i][j]) % mod
 
        return result

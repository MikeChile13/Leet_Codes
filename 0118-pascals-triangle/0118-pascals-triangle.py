class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for n in range(numRows):
            row = [1] * (n + 1)
            for k in range(1,n):
                row[k] = triangle[n - 1][k - 1] + triangle[n-1][k]
            
            triangle.append(row)
        
        return triangle
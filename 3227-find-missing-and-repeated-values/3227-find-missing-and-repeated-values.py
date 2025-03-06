class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])


        # Efficiently sort the grid using Cyclic sort
        for i in range(n):
            j = 0
            while j < n:
                if grid[i][j] != n*i + j+1:
                    row = math.ceil(grid[i][j] / n)
                    col = grid[i][j] % n
                    if not col:
                        col = n
                    
                    if grid[i][j] != grid[row - 1][col - 1]:
                        grid[i][j],grid[row - 1][col - 1] = grid[row-1][col - 1],grid[i][j]
                        continue
                j += 1
            
                
        # Find the missing and repeation values
        for r in range(n):
            for c in range(n):
                if grid[r][c] != n*r + c + 1:
                    return [grid[r][c], n*r + c + 1]
        return []


        
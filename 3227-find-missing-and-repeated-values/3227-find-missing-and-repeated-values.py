class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        val = (n*n) * ((n*n) + 1) // 2
        seen = set()
        res = []
        # print(val)
        for i in range(n):
            for j in range(n):
                if grid[i][j] in seen:
                    res.append(grid[i][j])
                else:
                    seen.add(grid[i][j])
                    val -= grid[i][j]
                
        res.append(val)
        return res


        
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        vals = []
        for row in grid:
            for val in row:
                if abs(val - grid[0][0]) % x != 0:
                    return -1
                vals.append(val)
        vals.sort()
        count = 1
        left_operations = [0] 

        for i in range(1,len(vals)):

            diff = vals[i] - vals[i-1]
            opp = diff//x

            left_operations.append(left_operations[i-1]+count*opp)
            count += 1

        min_val = left_operations[-1]
        count = 1
        right_operations = 0
        for i in range(len(vals)-2,-1,-1):
            diff = vals[i+1] - vals[i]
            right_operations += (diff//x) * count 
            min_val = min(min_val,left_operations[i] + right_operations)
            count += 1
        
        return min_val

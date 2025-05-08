class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        def solve(blocks, k,n):
    
            operations = 0
            for i in range(k):
                operations += (blocks[i] == 'W')
            
            minimum_operations = operations
            for i in range(k,n):
                operations += (blocks[i] =='W')
                operations -= (blocks[i-k] =='W')
                
                minimum_operations = min(minimum_operations, operations)
                
            return minimum_operations
        
        return solve(blocks,k,len(blocks))
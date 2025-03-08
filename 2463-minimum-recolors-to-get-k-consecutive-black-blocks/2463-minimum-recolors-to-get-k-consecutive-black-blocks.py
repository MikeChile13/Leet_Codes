class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i,j = 0,0
        changes = 0
        n = len(blocks)
        for j in range(k):
            if blocks[j] == "W":
                changes +=1
        j+=1
        min_changes = changes
        while j < n:
            if blocks[j] == blocks[i]:
                j+=1
                i+=1
                continue
            elif blocks[i] == "W":
                changes-=1
                min_changes = min(min_changes,changes)
                
            else:
                changes +=1
            j+=1
            i+=1
        return min_changes
        
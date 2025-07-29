class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        mydist = abs(target[0]) + abs(target[1])
        closestGhost = float('inf')
        for x,y in ghosts:
            closestGhost = min(abs(target[0]-x)+abs(target[1]-y),closestGhost)
            if closestGhost <= mydist:
                return False
        return True
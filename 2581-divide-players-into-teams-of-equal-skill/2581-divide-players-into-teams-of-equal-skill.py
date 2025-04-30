class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)

        if n == 2:
            return skill[0] * skill[1]
        total = sum(skill)
        # print(total)
        if total% (n//2):
            return -1
        
        skill_needed = total // (n//2)

        mapv = dict()

        res = 0
        for num in skill:
            if mapv.get(num, 0) > 0:
                res += num * (skill_needed - num)
                mapv[num] -= 1
            else:
                mapv[skill_needed - num] = mapv.get(skill_needed - num, 0) + 1
        
        for count in mapv.values():
            if count != 0:
                return -1
            
        # print(mapv)
        return res

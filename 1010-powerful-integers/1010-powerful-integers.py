class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if not bound:
            return []
        vals = set()
        
        power_x = math.floor(math.log(bound,x)) if x > 1 else 1
        power_y = math.floor(math.log(bound,y)) if y > 1 else 1
        for p1 in range(power_x+1):
            for p2 in range(power_y+1):
                test = x**p1 + y**p2
                if test <= bound and test not in vals:
                    vals.add(test)
                # print('iteration')
        # print(vals)
        return list(vals)
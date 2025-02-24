class Solution:
    def grayCode(self, n: int) -> List[int]:
        # https://www.youtube.com/watch?v=xG8qJ_U0XPg
        if n == 1:
            return [0,1]
        base = ['00','01','11','10']
        for _ in range(2,n):
            copy = base.copy()
            for i in range(len(base)):
                base[i] = '0' + base[i]
            for i in range(len(base)):
                copy[i] = '1' + copy[i]
            base.extend(copy[::-1])
        return [int(val,2) for val in base]
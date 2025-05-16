class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        output = [[rStart,cStart]]
        n = rows * cols
        printed = 1
        span = 1
        toggle = 1
        def inBound(row,col):
            if 0 <= row < rows and 0 <= col < cols:
                return True
            return False
        while printed < n:
            if toggle:
                for _ in range(span):
                    cStart += 1
                    if inBound(rStart,cStart):
                        output.append([rStart,cStart])
                        printed += 1
                for _ in range(span):
                    rStart += 1
                    if inBound(rStart,cStart):
                        output.append([rStart,cStart])
                        printed += 1
            else:
                for _ in range(span):
                    cStart -= 1
                    if inBound(rStart,cStart):
                        output.append([rStart,cStart])
                        printed += 1
                for _ in range(span):
                    rStart -= 1
                    if inBound(rStart,cStart):
                        output.append([rStart,cStart])
                        printed += 1
            span += 1
            toggle ^= 1
        return output


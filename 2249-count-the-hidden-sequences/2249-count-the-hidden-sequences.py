class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        x = y = current = 0
        for diff in differences:
            current += diff
            x = min(x, current)
            y = max(y, current)
            if y - x > upper - lower:
                return 0
        

        return (upper - lower) - (y - x) + 1

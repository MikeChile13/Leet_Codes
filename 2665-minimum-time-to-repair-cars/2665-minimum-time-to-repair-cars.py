class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def fixTime(mid):
            count = 0
            for r in ranks:
                count += int(math.sqrt(mid/r))
            
            # print(mid,count)
            return count >= cars

        n = math.ceil(len(ranks)/cars)
        left,right = 1, max(ranks)*cars**2

        res = 0
        while left <= right:
            mid = left + (right - left)//2

            if fixTime(mid):
                right = mid - 1     
            else:
                left = mid + 1
                res = mid
        return res + 1

    
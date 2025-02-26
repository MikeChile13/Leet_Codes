class Solution:
    def eatPile(self,k,nums,h):
        h1 = 0
        for bananas in nums:
            h1 += ceil(bananas/k)
            if h1 > h:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        top = max(piles)

        def searchK(left,right):
            while left <= right:
                mid = left + (right - left)//2
                v = self.eatPile(mid,piles,h)
                if v:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        return searchK(1,top)



class Solution:
    def eatPile(self,k,nums,h):
        h1 = 0 #h1 will be time taken to eat the pile for given K value
        for bananas in nums:
            h1 += ceil(bananas/k)#ceil because if there's a remainder Koko takes an extra hour to eat the remainder.
            if h1 > h:
                return False # if h1 exceeds we know our K value is too small.
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        top = max(piles) # the largest K value is the largest in the piles.

        def searchK(left,right): #binary search for K values
            while left < right:
                mid = left + (right - left)//2
                
                if self.eatPile(mid,piles,h): 
                    right = mid
                else:
                    left = mid + 1
            return left
        return searchK(1,top)



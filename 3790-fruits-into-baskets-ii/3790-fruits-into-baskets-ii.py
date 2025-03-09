class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used = set()
        placed = 0
        for fruit in fruits:
            for i in range(len(fruits)):
                if fruit <= baskets[i] and i not in used :
                    used.add(i)
                    # print(basket,fruit)
                    placed +=1
                    break
        # print(len(baskets),c,used)
        return len(fruits) - placed
        
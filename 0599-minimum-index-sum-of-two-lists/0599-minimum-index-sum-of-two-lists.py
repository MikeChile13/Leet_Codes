class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        indices = {word:idx for idx,word in enumerate(list1)}

        minv = float('inf')
        res = []
        for idx, word in enumerate(list2):
            if word in indices:
                current_sum = idx + indices[list2[idx]]

                if current_sum < minv:
                    minv = current_sum
                    res = [word]
                elif current_sum == minv:
                    res.append(word)
        return res


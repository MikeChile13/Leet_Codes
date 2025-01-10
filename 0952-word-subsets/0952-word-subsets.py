class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        wordset = {}
        for word in words2:
            freq = Counter(word)
            for key,val in freq.items():
                wordset[key] = max(wordset.get(key,0),val)
        ans = []
        for word in words1:
            freq = Counter(word)
            for key,value in wordset.items():
                if freq.get(key,0) < value:
                    break
            else:        
                ans.append(word)
        return ans 
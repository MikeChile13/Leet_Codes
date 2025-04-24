class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        top = 'qwertyuiopQWERTYUIOP'
        middle = 'asdfghjklASDFGHJKL'
        bottom = 'zxcvbnmZXCVBNM'
        mapv = defaultdict(int)
        
        for char in top:
            mapv[char] = 1
        for char in middle:
            mapv[char] = 2
        for char in bottom:
            mapv[char] = 3
        res = []
        for word in words:
            set_ = set()
            for c in set(word):
                set_.add(mapv[c])
            if len(set_) == 1:
                res.append(word)
        return res
            
            
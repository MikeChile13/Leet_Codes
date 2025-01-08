class Solution:
    def prefsuf(self,str1,str2) -> int:
        return str2.startswith(str1) and str2.endswith(str1)
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if len(words[i]) <= len(words[j]):
                    count += self.prefsuf(words[i],words[j])
        return count

from itertools import zip_longest
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1,s2 = s1.split(' '),s2.split(' ')
        freq = defaultdict(int)
        for word1,word2 in zip_longest(s1,s2, fillvalue = None):
            if word1 is not None:
                freq[word1]+=1
            if word2 is not None:
                freq[word2]+=1
        return [ans for ans,value in freq.items() if value == 1]
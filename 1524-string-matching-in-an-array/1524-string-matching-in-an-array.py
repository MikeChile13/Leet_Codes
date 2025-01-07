class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j or len(words[i]) > len(words[j]):
                    continue
                if words[j].find(words[i]) != -1:
                    ans.add(words[i])
        return list(ans)
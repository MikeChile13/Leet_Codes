class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        n = len(words)
        wordset = set(words)

        def find_substrings(word) -> None:
            for i in range(len(word)):
                current = ''
                for j in range(i,len(word)):
                    current+=word[j]
                    if current in wordset and len(current) < len(word):
                        ans.append(current)
                        wordset.remove(current)
        for i in range(n):
            if words[i] in wordset:
                find_substrings(words[i])

        return ans
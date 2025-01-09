class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for word in words:
            if len(word) <= len(s) and s.startswith(word):
                count+=1
        return count
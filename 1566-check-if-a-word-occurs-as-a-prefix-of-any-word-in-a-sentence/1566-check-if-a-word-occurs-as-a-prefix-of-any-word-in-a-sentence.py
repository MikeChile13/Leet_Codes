class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        n = len(searchWord)
        for i,word in enumerate(sentence.split(' ')):
            if n <= len(word):
                if word.startswith(searchWord):
                    return i+1
        return -1
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        total = 0
        for word in words:
            wcount = Counter(word)
            # If any character in wcount appears more times than in chars_count, word is not formable
            for ch, cnt in wcount.items():
                if cnt > chars_count.get(ch, 0):
                    break
            else:
                total += len(word)
        return total
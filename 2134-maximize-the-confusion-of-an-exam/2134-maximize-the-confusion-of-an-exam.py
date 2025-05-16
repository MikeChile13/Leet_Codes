class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def max_len_char(char):
            left = 0
            count = 0

            for right in range(len(answerKey)):
                if answerKey[right] != char:
                    count += 1
                if count > k:
                    if answerKey[left] != char:
                        count -= 1
                    left += 1
            return right - left + 1

        return max(max_len_char('T'),max_len_char('F'))

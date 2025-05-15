class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''
        values = '~!@#$%^&*()_+-={}|[]\\:";\'<>,.?/ `'
        for char in s:
            if char in values:
                continue
            new_string = new_string + char.lower()
        print(new_string)
        return new_string == new_string[::-1]
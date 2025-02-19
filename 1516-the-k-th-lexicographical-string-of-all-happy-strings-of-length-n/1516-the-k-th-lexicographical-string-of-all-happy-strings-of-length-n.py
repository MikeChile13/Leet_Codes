class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        if 3*(2**(n-1)) < k:
            return "" # Less than k happy strings

        if n == 1:
            return 'a' if k == 1 else 'b' if k == 2 else 'c'
        

        letters = ['a', 'b', 'c']
        res = []
        count = 0

        # Find which character should be in the FIRST position
        for j in range(3):
            _max = 2**(n-1)
            if count + _max < k:
                count += _max
            else:
                res.append(letters[j])
                break


        # Find which characters should be the remaining positions EXCEPT the LAST
        # Iterate through the positions from 1 to n-1
        for i in range(1, n - 1):
            
            # Go through the characters and try to put a character at current position
            for j in range(3):
                # If current character is the same as the previous do nothing
                if res[-1] == letters[j]:
                    continue

                # Get the maximun number of different happy strings that can be formed by placing letters[j] at position i
                _max = 2**(n - i - 1)
                if count + _max < k:
                    count += _max
                else:
                    # The smallest letter to be at current position is found
                    res.append(letters[j])
                    break

        # Find which character should be in the LAST position
        rem = k - count
        if rem == 1:
            if res[-1] == 'a':
                res.append('b')
            else:
                res.append('a')
        elif rem == 2:
            if res[-1] == 'a' or res[-1] == 'b':
                res.append('c')
            else:
                res.append('b')

        return "".join(res)
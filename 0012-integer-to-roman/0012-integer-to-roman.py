class Solution:
    def intToRoman(self, num: int) -> str:
        res = []
        num = str(num)
        length = len(num)
        ones = {
            '1':'I',
            '2':'II',
            '3':'III',
            '4':'IV',
            '5':'V',
            '6':'VI',
            '7':'VII',
            '8':'VIII',
            '9':'IX'
        }
        tens = {
            '1':'X',
            '2':'XX',
            '3':'XXX',
            '4':'XL',
            '5':'L',
            '6':'LX',
            '7':'LXX',
            '8':'LXXX',
            '9':'XC'
        }
        hundreds = {
            '1':'C',
            '2':'CC',
            '3':'CCC',
            '4':'CD',
            '5':'D',
            '6':'DC',
            '7':'DCC',
            '8':'DCCC',
            '9':'CM'
        }
        thousands = {
            '1':'M',
            '2':'MM',
            '3':'MMM'
        }
        index = [ones,tens,hundreds,thousands]
        for i in range(len(num)):
            if num[i] == '0':
                continue
            res.append(index[length-i-1][num[i]])

        return ''.join(res)
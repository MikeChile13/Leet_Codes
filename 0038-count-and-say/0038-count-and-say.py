class Solution:
    def recursion(self, n: int, target: int, val: str)-> str:
        if n == target:
            return val
        new_value = ''
        c = 1
        for i in range(1,len(val)):
            if val[i] == val[i-1]:
                c += 1
            else:
                new_value += str(c) + val[i-1]
                c = 1
        new_value += str(c) + val[-1]
        return self.recursion(n+1,target,new_value)

    def countAndSay(self, n: int) -> str:
        return self.recursion(1,n,'1')
        
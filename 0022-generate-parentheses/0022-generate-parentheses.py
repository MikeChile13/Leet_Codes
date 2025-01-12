class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(open,close,string):
            if open == 0 and close == 0:
                res.append(string)
                return
            if open == close:
                backtrack(open-1,close,string+'(')
            elif open:
                backtrack(open-1,close,string+'(')
                backtrack(open,close-1,string+')')
            elif close:
                backtrack(open,close-1,string+')')
        backtrack(n,n,'')
        return res
            


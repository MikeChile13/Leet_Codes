import re
class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            new = s.split('@')
            # print(new)
            return new[0][0] + '*****' + new[0][-1] + '@' + new[1]
        
        nums = ''
        for char in s:
            if char.isdigit():
                nums += char
            
        size = len(nums)
        if size > 10:
            return "+" + "*"*(size-10) + "-***-***-" + nums[-4:]
        return "***-***-"+ nums[-4:]
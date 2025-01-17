class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        last,first = 0,0
        for i in range(len(derived)-1):
            if derived[i] == 1:
                last = 1 if last == 0 else 0
            else:
                last = 0 if last == 0 else 1
        if derived[-1]:
            return first != last
        return first == last


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        original = [0]*len(derived)
        for i in range(len(derived)-1):
            if derived[i] == 1:
                original[i+1] = 0 if original[i] == 1 else 1
            else:
                original[i+1] = 1 if original[i] == 1 else 0
        if derived[-1] == 0:
            return original[-1] == original[0]
        else:
            return original[-1] != original[0] 
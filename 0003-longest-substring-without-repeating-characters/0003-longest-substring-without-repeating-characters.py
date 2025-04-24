class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_v = dict()
        max_len = 0
        length = len(s)
        j=1
        if not s:
            return 0
        if length <2:
            return 1

        hash_v[s[0]]=0
        while j < length:
            if s[j] not in hash_v:
                hash_v[s[j]]=j
                j+=1
                max_len = max(max_len,len(hash_v.keys()))
            elif next(iter(hash_v)) == s[j]:
                hash_v.pop(s[j])
            else:
                while next(iter(hash_v)) != s[j]:
                    hash_v.pop(next(iter(hash_v)))
        return max_len


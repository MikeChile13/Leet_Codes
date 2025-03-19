class Solution:
    def frequencySort(self, s: str) -> str:
        occurs = [0]*62

        for c in s:
            if 'a' <= c <= 'z':  # Lowercase letters
                occurs[ord(c) - ord('a')] += 1
            elif 'A' <= c <= 'Z':  # Uppercase letters
                occurs[ord(c) - ord('A') + 26] += 1
            else:
                occurs[int(c)+52] += 1
        max_heap = []
        for i,v in enumerate(occurs):
            if v:
                if i < 26:
                    c = chr(i+97)
                elif i < 52:
                    c = chr(i-26+65)
                else:
                    c = str(i-52)
                heapq.heappush(max_heap,(-v,c))
        res = ''
        while max_heap:
            v, c = heapq.heappop(max_heap)
            res += c * -v
        
        return res

class Solution:
    def largestInteger(self, num: int) -> int:
        odds = []
        odd_idx = []
        evens = []
        even_idx = []
        num = [int(v) for v in list(str(num))]
        for i in range(len(num)):
            if num[i] %2 == 0:
                evens.append(num[i])
                even_idx.append(i)
            else:
                odds.append(num[i])
                odd_idx.append(i)
        
        odds.sort(reverse=True)
        evens.sort(reverse=True)

        for i,even in enumerate(evens):
            num[even_idx[i]] = even
        for j,odd in enumerate(odds):
            num[odd_idx[j]] = odd
        ans = num[0]
        for i in range(1,len(num)):
            ans *= 10
            ans +=num[i]
        return ans
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):

            while stack and temperatures[stack[-1]] < temperatures[i]:
                val = stack.pop()
                ans[val] = abs(i-val)
            stack.append(i)
        return ans
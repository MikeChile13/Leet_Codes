class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0]
        prefix_sum = 0

        count = 1 if boxes[0] == '1' else 0

        for i in range(1,n):
            prefix_sum+=count
            res.append(prefix_sum)
            if boxes[i] == '1':
                count+=1
        
        count = 1 if boxes[-1] == '1' else 0
        suffix_sum = 0
        for i in range(n-2,-1,-1):
            suffix_sum+=count
            res[i]+=suffix_sum
            if boxes[i] == '1':
                count+=1
        
        return res

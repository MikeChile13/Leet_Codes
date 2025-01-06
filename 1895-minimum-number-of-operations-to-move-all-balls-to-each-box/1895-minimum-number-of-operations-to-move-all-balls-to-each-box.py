class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0]*n
        prefix_sum = 0

        count = 1 if boxes[0] == '1' else 0
        count1 = 1 if boxes[-1] == '1' else 0
        suffix_sum = 0
        for i in range(1,n):
            prefix_sum+=count
            suffix_sum+=count1
            res[i] +=prefix_sum
            res[n-i-1]+=suffix_sum
            if boxes[i] == '1':
                count+=1
            if boxes[n-i-1] == '1':
                count1+=1

        return res

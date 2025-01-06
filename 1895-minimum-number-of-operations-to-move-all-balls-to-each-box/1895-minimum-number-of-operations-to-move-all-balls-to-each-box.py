class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        forward = [0]*n
        backward = [0]*n

        count = 1 if boxes[0] == '1' else 0

        for i in range(1,n):
            forward[i] = forward[i-1] + count
            if boxes[i] == '1':
                count+=1
        
        count = 1 if boxes[-1] == '1' else 0

        for i in range(n-2,-1,-1):
            backward[i] = backward[i+1] + count
            if boxes[i] == '1':
                count+=1
        
        return [forward[i]+backward[i] for i in range(n)]

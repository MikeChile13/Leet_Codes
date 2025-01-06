class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        moves = []
        for i in range(len(boxes)):
            move = 0
            for j in range(len(boxes)):
                if j==i:
                    continue
                if boxes[j] == '1':
                    move+= abs(j-i)
            moves.append(move)
        return moves 
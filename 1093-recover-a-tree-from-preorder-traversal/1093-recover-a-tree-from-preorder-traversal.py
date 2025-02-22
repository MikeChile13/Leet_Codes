# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.index = 0

    def createTree(self, prev_height: int, arr: List[int]) -> Optional[TreeNode]:
        
        if self.index == len(arr) or prev_height+1 != arr[self.index][0]:
            return None

        node = TreeNode(arr[self.index][1])
        self.index+=1
        node.left = self.createTree(prev_height+1,arr)
        node.right = self.createTree(prev_height+1,arr)

        return node

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        arr = []
        height = 0
        index = 0
        current_num = traversal[0]

        for i in range(1,len(traversal)):
            if traversal[i].isnumeric():
                current_num+=traversal[i]
            elif traversal[i-1].isnumeric():
                arr.append((height,int(current_num)))
                height = 1
                current_num = ''
            else:
                height+=1

        arr.append((height,int(current_num)))
        
        return self.createTree(-1,arr)

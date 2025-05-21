# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.res.append(root.val)
        return
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.postorder(root)
        return self.res
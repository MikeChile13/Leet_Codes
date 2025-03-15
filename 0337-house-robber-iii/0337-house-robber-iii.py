# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        return self.dfs(root,False,memo)

    def dfs(self,root: Optional[TreeNode] ,parent_robbed: bool, memo: dict) -> int:

        if not root:
            return 0

        rob = 0
        if (root,parent_robbed) in memo:
            return memo[(root,parent_robbed)]
        if not parent_robbed:
            rob = root.val + self.dfs(root.left,True,memo) + self.dfs(root.right,True,memo)

        skip = self.dfs(root.left,False,memo) + self.dfs(root.right,False,memo)

        memo[(root,parent_robbed)] = max(rob,skip)
        return memo[(root,parent_robbed)]

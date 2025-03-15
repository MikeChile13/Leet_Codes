# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root))

    def dfs(self,root: Optional[TreeNode]) -> int:
        if not root:
            return [0,0]

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        with_root = root.val + left[1] + right[1]

        without_root = max(left) + max(right)

        return [with_root,without_root] 
# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node is None:
                return None, 0

            leftLCA, depthL = dfs(node.left)
            rightLCA, depthR = dfs(node.right)

            if depthL == depthR:
                return node, depthL + 1

            if depthL > depthR:
                return leftLCA, depthL + 1

            return rightLCA, depthR + 1
        
        lca, _ = dfs(root)
        return lca
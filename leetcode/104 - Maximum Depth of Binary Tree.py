# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, tree, level):
        if not tree:
            return level
        return max(self.dfs(tree.left, level+1), self.dfs(tree.right, level+1))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
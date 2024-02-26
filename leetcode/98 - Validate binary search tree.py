# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if root:
            if root.left:
                self.dfs(root.left)
            self.inorder.append(root.val)
            if root.right:
                self.dfs(root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.inorder = []
        self.dfs(root)
        for i in range(1, len(self.inorder)):
            if self.inorder[i - 1] >= self.inorder[i]:
                return False
        return True


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compair(self, left, right):
        if left and right:
            if left.val != right.val:
                return False
            return self.compair(left.left, right.right) and self.compair(left.right, right.left)
        else:
            if left or right:
                return False
            return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.compair(root.left, root.right)

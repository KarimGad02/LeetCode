# Last updated: 24/11/2025, 17:27:11
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirrorTrees(t, r):
            if not t and not r:
                return True
            if t and r and t.val != r.val:
                return False
            elif (not t and r) or (not r and t):
                return False
            return mirrorTrees(t.left, r.right) and mirrorTrees(t.right, r.left)
        return mirrorTrees(root.left, root.right)
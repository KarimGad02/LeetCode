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
            if t and r:
                if t.val != r.val:
                    return False
            else:
                return False
            if not mirrorTrees(t.left, r.right):
                return False
            return mirrorTrees(t.right, r.left)
        return mirrorTrees(root.left, root.right)
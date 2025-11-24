# Last updated: 24/11/2025, 17:27:10
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if p and q:
            if p.val != q.val:
                return False
        else:
            return False
        left_flag = self.isSameTree(p.left, q.left)
        if not left_flag:
            return False
        right_flag = self.isSameTree(p.right, q.right)
        return right_flag
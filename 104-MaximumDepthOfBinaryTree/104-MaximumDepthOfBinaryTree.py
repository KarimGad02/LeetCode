# Last updated: 24/11/2025, 17:27:09
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        count = 0
        def traversing(root, count):
            nonlocal max_depth
            if not root:
                return 0
            if not root.left and not root.right:
                count += 1
                if count > max_depth:
                    max_depth = count
                return max_depth
            count += 1
            traversing(root.left, count)
            traversing(root.right, count)
            return max_depth
        return traversing(root, count)
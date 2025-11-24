# Last updated: 24/11/2025, 17:27:06
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root):
        min_depth = 0
        count = 0
        def traversing(root, count):
            nonlocal min_depth
            if not root:
                count -= 1
                return 0
            count += 1
            if not root.left and not root.right:
                if min_depth == 0:
                    min_depth = count
                else:
                    min_depth = min(min_depth, count)
                return min_depth
            traversing(root.left, count)
            traversing(root.right, count)
            return min_depth
        return traversing(root, count)

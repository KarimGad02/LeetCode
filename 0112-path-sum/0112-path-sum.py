# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):
        sum = 0
        flag = False
        def traversing(root, sum):
            nonlocal flag
            if not root:
                return
            sum += root.val
            if not root.left and not root.right:
                if sum == targetSum:
                    flag = True
                else:
                    sum -= root.val
            traversing(root.left, sum)
            traversing(root.right, sum)
            return flag
        return traversing(root, sum)
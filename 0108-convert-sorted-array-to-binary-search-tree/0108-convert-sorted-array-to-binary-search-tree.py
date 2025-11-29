# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l = 0
        r = len(nums)-1
        def build(l, r):
            if l > r:
                return
            mid = (l+r)//2
            root = TreeNode(nums[mid])
            root.left = build(l, mid-1)
            root.right = build(mid+1, r)
            return root
        return build(l, r)
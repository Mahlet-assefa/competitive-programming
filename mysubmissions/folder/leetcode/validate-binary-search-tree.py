# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left=None
        def helper(root):
            nonlocal left
            if not root:
                return True
            if not helper(root.left):
                return False
            if left and left.val>=root.val:
                return False
            left=root
            return helper(root.right)
        return helper(root)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root:
                if root.left and root.right:
                    return 1+min(helper(root.left),helper(root.right))
                elif root.left and not root.right:
                    return 1+helper(root.left)
                else:
                    return 1+helper(root.right)
                
            else:
                return 0
        return helper(root)
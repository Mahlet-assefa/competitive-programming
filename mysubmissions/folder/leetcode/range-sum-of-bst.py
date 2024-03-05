# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        summed=0
        if not root: 
            return 0
        if low<=root.val<=high:
            summed+=root.val 
            left=self.rangeSumBST(root.left, low, root.val) 
            right= self.rangeSumBST(root.right, root.val, high)
            summed=summed+left+right
            return summed

        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        else:
            return self.rangeSumBST(root.left, low, high)




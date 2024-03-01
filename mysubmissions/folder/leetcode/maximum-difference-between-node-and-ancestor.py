# Definition for a binary tree root.
# class Treeroot:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(root,mini,maxi):
            if not root:
                return 0
            if root:
                if root.val<mini:
                    mini=root.val
                if root.val>maxi:
                    maxi=root.val
                left=helper(root.left,mini,maxi)
                # print(left,"hey")
                # print(maxi,mini,root.left)
                right=helper(root.right,mini,maxi)
                # print(right,"bye")
            return max(maxi - mini, left, right)
        return helper(root, root.val, root.val)

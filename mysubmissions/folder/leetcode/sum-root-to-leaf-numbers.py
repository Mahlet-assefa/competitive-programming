# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stk=[]
        collect=[]
        def helper(root):
            stk.append(str(root.val))
            if root.left:
                helper(root.left)
                stk.pop()
            if root.right:
                helper(root.right)
                stk.pop()
            if not root.right and not root.left:
                collect.append(int("".join(stk)))
        helper(root)
        return sum(collect)
                

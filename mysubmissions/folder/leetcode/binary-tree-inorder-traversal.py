# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        def Traversal(node):
            if node:
                Traversal(node.left)
                arr.append(node.val)
                Traversal(node.right)
        Traversal(root)
        return arr
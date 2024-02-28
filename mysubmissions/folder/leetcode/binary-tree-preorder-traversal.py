# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self,root: Optional[TreeNode]) -> List[int]:
        arr=[]
        def Traversal(node):
            if node:
                arr.append(node.val)
                Traversal(node.left)
                Traversal(node.right)
        Traversal(root)
        return arr
        #more compacted solution will be below but we are creating the array every time
        # return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right) if root else []
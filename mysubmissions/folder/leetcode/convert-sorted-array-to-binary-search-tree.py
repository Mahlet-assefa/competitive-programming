# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def divide(l,r):
            n=len(nums)
            if l==r:
                root=TreeNode(nums[l])
                return root
            if l>r:
                return

            mid=(r+l)//2
            root=TreeNode(nums[mid])
            left=divide(l,mid-1)
            right=divide(mid+1,r)
            
            root.left=left
            root.right=right

            return root
        return divide(0,len(nums)-1)
       
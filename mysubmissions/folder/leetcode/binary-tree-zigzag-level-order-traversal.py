# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # if not root:
        #     return
        # if root and root.left==None and root.right==None:
        #     return
        my_dict=defaultdict(list)

        def helper(node,level):
            if node:
                helper(node.left,level+1)
                helper(node.right,level+1)
                my_dict[level].append(node.val)
        helper(root,0)
       
        my_sorted=dict(sorted(my_dict.items(), key=lambda x:x[0]))
       
        res=[]
        for key,val in my_sorted.items():
            #print(key)
            if key%2!=0:
                res.append(val[::-1])
            else:
                
                res.append(val)
        return res
                
       

            
        
            
            


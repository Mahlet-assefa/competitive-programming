# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        my_dict=defaultdict(int)
        def helper(root):
            if root:
                helper(root.left)
                helper(root.right)
                my_dict[root.val]+=1
            #print(my_dict)
        helper(root)
        arr=[]
        maxi=0
        for key,val in my_dict.items():
            if val>maxi:
                arr=[key]
                maxi=val
            elif val==maxi:
                arr.append(key)
        return arr
        #         if root.left:
        #             helper(root.left)
        #             if root.left.val==root.val:
        #                 my_dict[root.val]+=1
        #         my_dict[root.val]-=1
        #         if root.right:
                    
        #             if root.right.val==root.val:
        #                 my_dict[root.val]+=1
        #             my_dict[root.val]-=1
                
                
        #         arr.append(my_dict[maxi])
        
        # return arr
         


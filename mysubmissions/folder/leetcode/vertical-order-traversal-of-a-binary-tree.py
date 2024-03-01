# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        my_dict=defaultdict(list)
        pos=[0]
        depth=[0]
        def helper(root,pos,depth):
            my_dict[pos[0]].append([depth[0],root.val])
            
            if root.left:
                pos[0]-=1
                depth[0]+=1
                helper(root.left,pos,depth)
                depth[0]-=1
                pos[0]+=1
            
            if root.right:
                pos[0]+=1
                depth[0]+=1
                helper(root.right,pos,depth)
                pos[0]-=1
                depth[0]-=1
        helper(root,pos,depth)
        print(my_dict)
        for key in my_dict.keys():
            my_dict[key].sort()
        key = sorted(my_dict)
        ans=[]
        for i in key:
            temp=[c[1] for c in my_dict[i]]
            ans.append(temp)
        return ans

       
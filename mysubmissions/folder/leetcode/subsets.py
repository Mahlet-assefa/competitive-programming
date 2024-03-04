class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subsetsback(n,path):
            if len(path)<=len(nums):
                ans.append(path[:])
    
            for i in range(n,len(nums)):
                path.append(nums[i])
                subsetsback(i+1,path)
                path.pop()
        ans=[]
        subsetsback(0,[])
        return ans
            
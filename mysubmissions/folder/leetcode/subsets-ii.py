class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        my_set=set()
        def backsubsetsWithDup(n,path):
            if path and tuple(sorted(path)) in my_set:
                return
            my_set.add(tuple(sorted(path)))
            if len(path)<=len(nums):
                ans.append(path[:])

            for i in range(n,len(nums)):
                path.append(nums[i])
                backsubsetsWithDup(i+1,path)
                path.pop()
        ans=[]
        backsubsetsWithDup(0,[])
        return ans

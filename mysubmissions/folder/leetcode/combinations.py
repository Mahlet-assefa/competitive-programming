class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backcombine(first,path):
            if len(path)==k:
                ans.append(path[:])
                return
            for i in range(first,n+1):
                path.append(i)
                backcombine(i+1,path)
                path.pop()
        ans=[]
        backcombine(1,[])
        return ans

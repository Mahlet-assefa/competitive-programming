class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backcombinationSum(n,added):
            summed=0
            summed=sum(added)
            if summed==target:
                ans.append(added[:])
            elif summed>target:
                return
            for i in range(n,len(candidates)):
                added.append(candidates[i])
                backcombinationSum(i,added)
                added.pop()
        ans=[]
        backcombinationSum(0,[])
        return ans
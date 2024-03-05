class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        my_set=set()
        def backcombinationSum2(n,added):
            nonlocal my_set
            if added and tuple(sorted(added)) in my_set:
                return
            my_set.add(tuple(sorted(added)))
            summed=sum(added)
            if summed==target:
                ans.append(added[:])
                return
            elif summed>target:
                return
            
            for i in range(n,len(candidates)):
                added.append(candidates[i])
                backcombinationSum2(i+1,added)
                added.pop()
        ans=[]
        backcombinationSum2(0,[])
        return ans


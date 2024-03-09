class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n=len(arr)
        r=[n]*n
        l=[-1]*n
        stk=[]
        res=0
        for idx,val in enumerate(arr):
            while stk and arr[stk[-1]]>=val:
                stk.pop()
            if stk:
                l[idx]=stk[-1]
            stk.append(idx)
        stk=[]
        for idx in range(n-1,-1,-1):
            while stk and arr[stk[-1]] > arr[idx]:
                stk.pop()
            if stk:
                r[idx]=stk[-1]
            stk.append(idx)
        for idx,val in enumerate(arr):
            res+=(idx-l[idx])*(r[idx]-idx)*val
            res=res%(10**9 + 7)
        return res
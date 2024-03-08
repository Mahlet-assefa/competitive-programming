class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        r=len(nums)-1
        res=0
        for i in range(len(nums)):
            while nums[r]+nums[i]>target and i<=r:
                r-=1
            if i<=r:
                n=r-i
                res+=2**n
        return res%(10**9 + 7)
            
        #     l=0
        #     r=len(nums)
        #     while l+1<r:
        #         mid=(l+r)//2
        #         if nums[mid]<=diff:
        #             l=mid
        #         else:
        #             r=mid
        #     return l
        
             
        # for i in range(len(nums)):
        #     diff=target-nums[i]
        #     pos=bisector(diff)
        #     if pos-i>0:
        #         n=pos-i
        #         res+=2**n
        #     if res>=2:
        #     return res

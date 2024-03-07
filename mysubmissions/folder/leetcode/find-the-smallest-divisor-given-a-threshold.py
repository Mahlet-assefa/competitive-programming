class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l=0
        r=max(nums)
        
        while l+1<r:
            mid=(l+r)//2
            summed=0
            for i in range(len(nums)):
                summed+=ceil(nums[i]/mid)
            if summed>threshold:
                l=mid
            else: 
                r=mid
        return r
             


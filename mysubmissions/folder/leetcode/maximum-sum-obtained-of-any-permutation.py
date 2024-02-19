class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort()
        ans=[0]*len(nums)
        
        for start,end in requests:
            ans[start]+=1
            if end+1 < len(nums):
                ans[end+1]-=1
        for i in range(1,len(nums)):
            ans[i]+=ans[i-1]
        ans.sort()
        total=0
        for i in range(len(nums)):
            total+=nums[i]*ans[i]
        return (total)%(10**9 + 7)

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        i=0
        summed=0
        maxii=float("-inf")
        while i<len(nums):
            summed+=nums[i]
            avg=ceil(summed/(i+1))
            maxii=max(maxii,avg)
            print(avg)
            i+=1
        return maxii

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=-1
        r=len(nums)-1
        inserted=0
        while l+1<r:
            mid=(l+r)//2
            if nums[mid]>target:
                r=mid
            elif nums[mid]<target:
                l=mid
            else:
                return mid
        if target>nums[r]:
            return r+1
        else:
            return r
        return r
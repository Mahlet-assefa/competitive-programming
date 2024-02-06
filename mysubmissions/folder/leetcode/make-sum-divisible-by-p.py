class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        subarr = sum(nums) % p
        if not subarr:
            return 0
        res = len(nums)
        curr = 0 
        lookup = {0: -1}
        for i, num in enumerate(nums):
            curr = (curr+num) % p
            lookup[curr] = i
            if (curr-subarr) % p in lookup:
                res = min(res, i-lookup[(curr-subarr)%p])
        if res < len(nums): 
            return res
        else:
            return -1
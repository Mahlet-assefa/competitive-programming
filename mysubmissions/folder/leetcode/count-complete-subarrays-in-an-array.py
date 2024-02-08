class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = len(set(nums))
        ans=0 
        n = len(nums)
        for i in range(n):
            s = set()
            for x in nums[i:]:
                s.add(x)
                if len(s) == count:
                    ans += 1
        return ans
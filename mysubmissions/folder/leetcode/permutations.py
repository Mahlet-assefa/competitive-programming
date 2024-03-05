class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backpermute(path):
            if len(path)==len(nums):
                ans.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backpermute(path)
                    path.pop()
        ans=[]
        backpermute([])
        return ans


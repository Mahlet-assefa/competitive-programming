class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(nums, k):
            result, left, count = 0, 0, 0
            for right, x in enumerate(nums):
                count += x%2
                while count > k:
                    count -= nums[left]%2
                    left += 1
                result += right-left+1
            return result

        return atMost(nums, k) - atMost(nums, k-1)

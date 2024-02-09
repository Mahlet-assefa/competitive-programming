class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = 0
        curr_sum = 0
        for item in nums:
            curr_sum += item
            if curr_sum < 0:
                curr_sum = 0
            if curr_sum > max_sum:
                max_sum = curr_sum

        if max_sum == 0:
            max_sum = max(nums)
        return max_sum

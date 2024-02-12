class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        direction=1
        total = len(nums)

        for s in range(total):
            if type(nums[s]) == str:
                continue

            j = s
            if nums[j] > 0:
                direction = 1 
            else:
                direction=-1
            

            while type(nums[j]) == int and nums[j] * direction > 0 and nums[j] % total:
                j_next = (j + nums[j]) % total
                nums[j] = str(s)
                j = j_next
                if nums[j] == str(s):
                    return True

        return False
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ur=1
        patch=0
        r=0
        while ur<=n:
            if r<len(nums) and ur>=nums[r]:
                    ur+=nums[r]
                    r+=1
                    print(ur)

            else:
                ur*=2
                patch +=1
               
         
                # if ur>nums[-1]:
                #     break
        return patch
                

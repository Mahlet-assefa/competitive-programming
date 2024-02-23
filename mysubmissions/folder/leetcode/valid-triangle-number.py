class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        cnt=0
        k=0
        for k in range(len(nums)):
            right=len(nums)-1
            left=k+1
            while left<right:
                if nums[right]+nums[left]>nums[k]:
                    cnt+=right-left
                    left+=1
                else:
                    right-=1
        
        
        return cnt

            


        
     
                
        
            

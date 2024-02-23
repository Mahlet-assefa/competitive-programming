class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mini=float("inf") 
        leftarr=[]
        stk=[]
        for i in range(len(nums)):
            leftarr.append(mini)
            mini= min(mini,nums[i])
        #print(leftarr)
        for i in range(len(nums)-1,-1,-1):
            while stk and nums[i]>stk[-1]:
                x=stk.pop()
                if x>leftarr[i]:
                    return True
            stk.append(nums[i])
            
        return False           


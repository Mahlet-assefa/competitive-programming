class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk=[]
        n=len(nums)
        ans=[]*len(nums)
        my_dict=defaultdict(int)
        for idx,val in enumerate(nums):
            my_dict[(idx,val)]=-1
        
        for i in range(2*n):
            if not stk:
                stk.append((i%n,nums[i%n]))
            else:

                while stk and nums[i%n]>stk[-1][1]:
                    x=stk.pop()
                    my_dict[x]=nums[i%n]
                stk.append((i%n,nums[i%n]))
        
        print(my_dict)
        for idx,val in enumerate(nums):
            if (idx,val) in my_dict:
                ans.append(my_dict[(idx,val)])
        return ans



 # for i in range(len(nums)-1,-1,-1):
        #     rev.append(nums[i])
        # while stk and rev[-1]>stk[-1]:
        #     my_dict[stk[-1]]=rev[-1]
        #     stk.pop()
        # rev.pop()
       
        
                




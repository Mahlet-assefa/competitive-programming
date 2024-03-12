class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        my_dict={}
        for i in range(len(nums)):
            if nums[i] not in my_dict:
                my_dict[nums[i]]=[]
                my_dict[nums[i]].append(i)
            else:
                my_dict[nums[i]].append(i)
        res=[0]*len(nums)
        summed=0
        for key,val in my_dict.items():
            suffix=sum(val)
            prifix=0
            s=len(val)
            x=0
            ans=0
            for i in val:
                prifix+=i
                x+=1
                suffix-=i
                s-=1
                t=-prifix+x*i-s*i+suffix
                res[i]=t
        return res
        
        
            
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # ans=[-1]*len(nums1)
        # for i in range(len(nums1)-1):
        #     for j in range(len(nums2)-1):
        #         if nums1[i]==nums2[j]:
        #             if nums2[j+1]>nums1[i]:
        #                 ans.append(nums2[j+1])
        # return ans
        stk=[]
        ans=[]*len(nums1)
        my_dict=defaultdict(int)
        for i in nums1:
            my_dict[i]=-1
        for i in nums2:
            if not stk:
                stk.append(i)
            else:

                while stk and i>stk[-1]:
                    x=stk.pop()
                    my_dict[x]=i
                stk.append(i)
        for i in range(len(nums1)):
            if nums1[i] in my_dict:
                ans.append(my_dict[nums1[i]])
        return ans

       
        
                





                    


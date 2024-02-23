class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk=[]
        letters="abcdefghijklmnopqrstuvwxyz"
        n=len(s)
        ans=""
        my_dict=defaultdict(int)
        for i in s:
            my_dict[i]+=1
        
        for i in range(len(s)):
            if s[i] in stk:
                my_dict[s[i]]-=1
                continue
            if not stk:
                stk.append(s[i])
            else:
                while stk and letters.index(s[i])<letters.index(stk[-1]) and my_dict[stk[-1]]>1:
                        x=stk.pop()
                        my_dict[x]-=1
            
                stk.append(s[i])
        return "".join(stk)


        # for i in range(len(nums)):
        #     if nums[i] in my_dict:
        #         ans.append(my_dict[nums[i]])
        # return ans'
      
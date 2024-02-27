class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n=len(s)
        my_dict=defaultdict(int)
        for i in range(len(s)):
            my_dict[s[i]]=i
        # print(my_dict)
        curr=0
        output=[]
        while curr < n:
            end=my_dict[s[curr]]
            j=curr+1
            while j<end:
                end=max(end,my_dict[s[j]])
                j+=1
            
            output.append(end-curr+1) 
            curr=end+1
               
        return output

        
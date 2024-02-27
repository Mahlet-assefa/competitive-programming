class Solution:
    def decodeString(self, s: str) -> str:
        ans=[]
        def helper(i):
            arr=[]
            num=[]
            while s[i]!="[":
                num.append(s[i])
                i+=1
            num=int("".join(num))
            i+=1

            output=[]
            while s[i] != "]":
                if s[i].isdigit():
                    x=helper(i)
                    output.append(x[0])
                    i=x[1]

                else:
                    output.append(s[i])
                    i+=1

            output="".join(output)
            arr.append(output*num)

            return "".join(arr),i+1
        i=0
        while i<len(s):
            if s[i].isdigit():
                x=helper(i)
                ans.append(x[0])
                i=x[1]

            else:
                ans.append(s[i])
                i+=1
        return "".join(ans)

